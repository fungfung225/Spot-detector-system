from DetectorApp import *

if __name__ == '__main__':
    Log("FabricDefectsDetection", level=logging.INFO)
    exit_code = -999
    try:
        app = DetectorApp()
        exit_code = app.launch()
    except Exception as e:
        logging.exception(f"Critical exception {e} caught in main.py:")
        print(e)

    # Update log one more time to include exception message
    service = create_service_service_account(GoogleDriveResultHandler.CLIENT_SECRET_FILE,
                                             GoogleDriveResultHandler.API_NAME, GoogleDriveResultHandler.API_VERSION,
                                             GoogleDriveResultHandler.SCOPES)

    detection_upload_folder_id = gd_create_folder_if_not_exist(f'{platform.node()}_detection',
                                                               '18GxXYaFE7QfyUSA7MBITpUC0QSUuGMGs', service)
    gd_log_folder_id = gd_create_folder_if_not_exist("Running_logs", detection_upload_folder_id, service)
    gd_log_files = gd_get_all_files(gd_log_folder_id, service)
    local_log_files = get_all_files("logs")
    for log in local_log_files:
        if log not in gd_log_files:
            gfile_id = gd_upload_file(f"logs/{log}", gd_log_folder_id, service)
            if gfile_id is None:
                Log.warning(f"logs/{log} upload failed.")
        else:
            gfile_id = gd_update_file(f'logs/{log}', gd_log_files[log], service)
            # delete previous local log
            if log not in Log.LOG_FILE and gfile_id is not None:
                os.remove(f"logs/{log}")
    if exit_code == 999:
        os.system('poweroff')
    elif exit_code == 888:
        os.system('reboot')

    sys.exit(exit_code)
