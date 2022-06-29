from libs.GoogleDrive import *
from libs.ThreadRunnable import *
from libs.utils import *


class GoogleDriveResultHandler(Debugable, ThreadRunnable):
    _RESULT_DIR = f'{platform.node()}_detection'
    CLIENT_SECRET_FILE = "res/spot-v2-service-account.json"
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    APP_FOLDER_ID = '18GxXYaFE7QfyUSA7MBITpUC0QSUuGMGs'  # 我的雲端硬碟 -> 異物檢測

    SYNC_INTERVAL = 1800  # auto sync record every 1800 sec

    def sync_log(self):
        self.service = create_service_service_account(self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION,
                                                      self.SCOPES)
        gd_log_folder_id = gd_create_folder_if_not_exist("Running_logs", self.detection_upload_folder_id, self.service)
        gd_log_files = gd_get_all_files(gd_log_folder_id, self.service)
        local_log_files = get_all_files("logs")
        for log in local_log_files:
            if log not in gd_log_files:
                gfile_id = gd_upload_file(f"logs/{log}", gd_log_folder_id, self.service)
                if gfile_id is None:
                    Log.warning(f"logs/{log} upload failed.")
            else:
                gfile_id = gd_update_file(f'logs/{log}', gd_log_files[log], self.service)
                # delete previous local log
                if log not in Log.LOG_FILE and gfile_id is not None:
                    os.remove(f"logs/{log}")

    def exit_nicely(self, *args):
        Log.info("Synchronizing data to Google drive... Please wait.")
        self.sync_gd_from_local()
        Log.info(f"Synchronizing data to Google drive done!")
        Log.info("Google drive thread terminated.")
        rm_empty_dirs(self.result_dir)

    def on_start(self):
        Log.info("Google drive result handler thread started.")

    def main_body(self):
        Log.info("Synchronizing to Google drive...")
        self.sync_gd_from_local()
        self.sync_log()
        Log.info(f"Synchronizing detected imgs to Google drive done! Next synchronization in {self.SYNC_INTERVAL}s.")
        for i in range(self.SYNC_INTERVAL):
            if not self.loop_run:
                break
            time.sleep(1)

    def on_end(self):
        self.exit_nicely()

    def __init__(self):
        Debugable.__init__(self)
        ThreadRunnable.__init__(self)

        self.result_dir = self._RESULT_DIR
        create_dir_if_not_exists(self.result_dir)

        rm_empty_dirs(self.result_dir)

        self.service = create_service_service_account(self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION,
                                                      self.SCOPES)
        self.detection_upload_folder_id = gd_get_object_id(self.result_dir, self.APP_FOLDER_ID, self.service)

        if self.detection_upload_folder_id is None:
            self.detection_upload_folder_id = gd_create_folder(self.result_dir, self.APP_FOLDER_ID, self.service)

        self.gd_uploaded_result_folders_dict = {}
        self.local_detection_result_dirs_lst = []

    def update_folders_dirs(self):
        self.service = create_service_service_account(self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION,
                                                      self.SCOPES)
        self.gd_uploaded_result_folders_dict = gd_get_all_sub_folders(self.detection_upload_folder_id, self.service)
        self.local_detection_result_dirs_lst = get_all_subdir(self.result_dir)

    def sync_gd_from_local(self):
        self.update_folders_dirs()
        if self.local_detection_result_dirs_lst is None:
            return
        for local_dir in self.local_detection_result_dirs_lst:
            local_dir_path = self.result_dir + '/' + local_dir
            local_files = get_all_files(local_dir_path)
            if len(local_files) < 1:
                continue
            if local_dir in self.gd_uploaded_result_folders_dict:
                gd_files = gd_get_all_files(self.gd_uploaded_result_folders_dict[local_dir], self.service)
                for file in local_files:
                    img_file = local_dir_path + "/" + file
                    if file not in gd_files:
                        ret = gd_upload_file(img_file, self.gd_uploaded_result_folders_dict[local_dir], self.service)
                        if ret is not None:
                            os.remove(img_file)
                    else:
                        os.remove(img_file)
            else:
                gd_folder_id = gd_create_folder(local_dir, self.detection_upload_folder_id, self.service)
                for file in local_files:
                    img_file = local_dir_path + "/" + file
                    ret = gd_upload_file(img_file, gd_folder_id, self.service)
                    if ret is not None:
                        os.remove(img_file)
            # If it can't connect to the internet for 3 days
            if get_creation_time(time.time() - get_creation_time(local_dir_path) > 3 * 24 * 3600):
                rm_rf_dir(local_dir_path)
