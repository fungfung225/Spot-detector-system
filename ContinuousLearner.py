"""
Upload captured raw image, download the latest trained weight.
"""
import gspread

from libs.GoogleDrive import *
from libs.ThreadRunnable import ThreadRunnable
from libs.utils import *

LOCAL_WEIGHTS_PATH = 'res/download_weights/'


class ContinuousLearner(ThreadRunnable):
    def exit_nicely(self, *args):
        self.thread_stop()
        Log.info("Synchronizing raw data to Google drive... Please wait.")
        self._sync_raw_to_gd()
        Log.info(f"Synchronizing raw data to Google drive done!")
        rm_empty_dirs(self.TRAINING_RAW_DIR)
        for thr in self.download_threads:
            thr.join()

    def on_start(self):
        Log.info("Google drive data handler thread started.")
        thr = self.try_download_general_weights()
        if thr is not None:
            self.download_threads.append(thr)
        thr = self.try_download_my_weights()
        if thr is not None:
            self.download_threads.append(thr)

    def sync_raw_to_gd_now(self):
        Log.info("Sync raw data to Google drive now!")
        self.sync_now = True

    def main_body(self):
        Log.info("Synchronizing raw to Google drive...")
        self._sync_raw_to_gd()
        self.sync_now = False
        Log.info(f"Synchronizing raw imgs to Google drive done!")
        for i in range(self.SYNC_INTERVAL):
            self.get_local_raw_img_dir_today()
            if not self.loop_run or self.sync_now:
                break
            time.sleep(1)

    def on_end(self):
        self.exit_nicely()

    SYNC_INTERVAL = 10800  # sync every 3 hours
    CLIENT_SECRET_FILE = "res/spot-v2-service-account.json"
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    NUM_RAW_DAILY = 400  # collect 400 raw images a day
    KEEP_DAYS = 7  # keep the imgs 7 days if failed to upload

    # noinspection SpellCheckingInspection
    APP_FOLDER_ID = '1Al5SyzlX0D4mhdCumA9yiflqsTaCRbEj'
    G_SHEET_ID = '1XlbGvEBC5t_4GMAfEsDu-cBkp8I_yrt_K0V7NrSgNlE'  # Trained Weights' Google Sheets ID

    NODE_FOLDER = f'{platform.node()}'
    TRAINING_RAW_DIR = f'raw_imgs'
    raw_img_dir_today = TRAINING_RAW_DIR + f"/{get_date_today()}"

    def __init__(self):
        super().__init__()
        create_dir_if_not_exists(self.raw_img_dir_today)
        self.gd_service = self.new_service()
        self.gd_node_folder = gd_create_folder_if_not_exist(self.NODE_FOLDER,
                                                            self.APP_FOLDER_ID,
                                                            self.gd_service)
        self.gd_raw_folder_id = gd_create_folder_if_not_exist(self.TRAINING_RAW_DIR,
                                                              self.gd_node_folder,
                                                              self.gd_service)
        self.local_raw_dirs_lst = []
        self.gd_uploaded_raw_zip_dict = {}
        self.update_raw_folders_dirs()
        self.upload_timestamp = time.time()
        self.new_raw_timestamp = time.time() + 1
        self.sync_now = False

        self.gc = gspread.service_account(filename='res/spot-v2-service-account.json')
        self.g_sht = self.gc.open_by_key(self.G_SHEET_ID)
        self.general_table = self.g_sht.worksheet("General")
        try:
            self.my_table = self.g_sht.worksheet(platform.node())
        except gspread.exceptions.WorksheetNotFound:
            self.my_table = self.g_sht.add_worksheet(platform.node(), 2, 20)
            self.my_table.update('A1:E1', [
                ['My Weights File ID', 'Update Int Time', 'Update Time', 'Download Int Time', 'Download Time']])
        self.download_threads = []

    def record_new_raw_timestamp(self):
        self.new_raw_timestamp = time.time()

    def get_local_raw_img_dir_today(self):
        self.raw_img_dir_today = self.TRAINING_RAW_DIR + f"/{get_date_today()}"
        create_dir_if_not_exists(self.raw_img_dir_today)
        return self.raw_img_dir_today

    def get_num_collected_raw_today(self):
        self.get_local_raw_img_dir_today()
        num_local = len(get_all_files(self.get_local_raw_img_dir_today()))
        return num_local

    def get_raw_target_today(self):
        return self.NUM_RAW_DAILY - self.get_num_collected_raw_today()

    def new_service(self):
        self.get_local_raw_img_dir_today()
        return create_service_service_account(self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION, self.SCOPES)

    def update_raw_folders_dirs(self):
        self.gd_service = self.new_service()
        self.gd_uploaded_raw_zip_dict = gd_get_all_files(self.gd_raw_folder_id, self.gd_service)
        self.local_raw_dirs_lst = get_all_subdir(self.TRAINING_RAW_DIR)

    def _sync_raw_to_gd(self):
        if self.upload_timestamp > self.new_raw_timestamp:
            return
        self.update_raw_folders_dirs()
        if self.local_raw_dirs_lst is None:
            return
        for raw_dir in self.local_raw_dirs_lst:
            full_local_dir_path = self.TRAINING_RAW_DIR + f'/{raw_dir}'
            local_files = get_all_files(full_local_dir_path)
            if len(local_files) < 1:
                continue
            os.system(f"cd {self.TRAINING_RAW_DIR}; zip -r {raw_dir}.zip {raw_dir}/")
            full_local_zip_path = full_local_dir_path + '.zip'
            gd_zip_id = gd_get_object_id(raw_dir + '.zip', self.gd_raw_folder_id, self.gd_service)

            if gd_zip_id is None:
                ret = gd_upload_file(full_local_zip_path, self.gd_raw_folder_id, self.gd_service)
            else:
                ret = gd_update_file(full_local_zip_path, gd_zip_id, self.gd_service)

            if ret is not None:
                os.remove(full_local_zip_path)
                if full_local_dir_path != self.raw_img_dir_today:
                    rm_rf_dir(full_local_dir_path)
            elif get_creation_time(time.time() - get_creation_time(full_local_dir_path) > 3 * 24 * 3600):
                # If it can't connect to the internet for 3 days
                os.remove(full_local_zip_path)
                rm_rf_dir(full_local_dir_path)
        self.upload_timestamp = time.time()

    def get_general_weights_upload_time(self):
        if get_ram_size_gb() < 3:
            return self.general_table.acell('B2').value
        else:
            return self.general_table.acell('B3').value

    def get_general_weights_file_id(self):
        if get_ram_size_gb() < 3:
            return self.general_table.acell('A2').value
        else:
            return self.general_table.acell('A3').value

    def get_general_weights_download_time(self):
        node_cell = self.general_table.find(platform.node())
        return None if node_cell is None else self.general_table.cell(node_cell.row, node_cell.col + 1).value

    def update_general_weights_download_time(self):
        node_cell = self.general_table.find(platform.node())
        if node_cell is None:
            node_col = self.general_table.col_values(6)
            self.general_table.update_cell(len(node_col) + 1, 6, platform.node())
            self.general_table.update_cell(len(node_col) + 1, 7, int(time.time()))
            self.general_table.update_cell(len(node_col) + 1, 8, get_current_time())
        else:
            self.general_table.update_cell(node_cell.row, node_cell.col + 1, int(time.time()))
            self.general_table.update_cell(node_cell.row, node_cell.col + 2, get_current_time())
        Log.info(f'General weights file downloaded.')

    def try_download_general_weights(self):
        upload_time = self.get_general_weights_upload_time()
        if upload_time is None or int(upload_time) < 1:
            return None
        download_time = self.get_general_weights_download_time()
        if download_time is None or int(upload_time) > int(download_time):
            weights_file_id = self.get_general_weights_file_id()
            if weights_file_id is not None:
                service = self.new_service()
                create_dir_if_not_exists(LOCAL_WEIGHTS_PATH)
                return gd_download_file_async(LOCAL_WEIGHTS_PATH + '/general.engine', weights_file_id, service,
                                              self.update_general_weights_download_time)
        return None

    def try_download_my_weights(self):
        upload_time = self.get_my_weights_upload_time()
        if upload_time is None or int(upload_time) < 1:
            return None
        download_time = self.get_my_weights_download_time()
        if download_time is None or int(upload_time) > int(download_time):
            weights_file_id = self.get_my_weights_file_id()
            if weights_file_id is not None:
                service = self.new_service()
                create_dir_if_not_exists(LOCAL_WEIGHTS_PATH)
                return gd_download_file_async(LOCAL_WEIGHTS_PATH + f'/{platform.node()}.engine', weights_file_id,
                                              service,
                                              self.update_my_weights_download_time)
        return None

    def get_my_weights_upload_time(self):
        return self.my_table.acell('B2').value

    def get_my_weights_download_time(self):
        return self.my_table.acell('D2').value

    def get_my_weights_file_id(self):
        return self.my_table.acell('A2').value

    def update_my_weights_download_time(self):
        self.my_table.update_acell('D2', int(time.time()))
        self.my_table.update_acell('E2', get_current_time())
        Log.info(f'My weights file downloaded.')


if __name__ == '__main__':
    gddh = ContinuousLearner()
    print("General weights upload time:", gddh.get_general_weights_upload_time())
    print("General weights download time:", gddh.get_general_weights_download_time())
    print("My weights upload time:", gddh.get_my_weights_upload_time())
    print("My weights download time:", gddh.get_my_weights_download_time())
    gddh.try_download_general_weights()
    gddh.try_download_my_weights()

    # gddh._sync_raw_to_gd()
    # print(f"today target = {gddh.get_raw_target_today()}")
    # gddh.thread_start()
    # time.sleep(5)
    # gddh.sync_raw_to_gd_now()
    # time.sleep(5)
    # gddh.thread_stop()
    # gddh.thread_join()
