import datetime
import io
import threading
import traceback

import apiclient
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from oauth2client.service_account import ServiceAccountCredentials

from libs.GoogleMIME import *
from libs.Log import *
from libs.utils import *

TOKEN_PATH = str(Path.home()) + '/token_google_drive.json'

MIME_FILE = 'application/vnd.google-apps.file'  # Google Drive file
MIME_FOLDER = 'application/vnd.google-apps.folder'  # Google Drive folder


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt


def create_service_service_account(client_secret_file, api_name='drive', api_version='v3', *scopes):
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    try:
        cred = ServiceAccountCredentials.from_json_keyfile_name(client_secret_file, scopes=SCOPES)
        service = apiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        return service
    except Exception as e:
        Log.error(
            f"Catching exception when creating google service with service account ({CLIENT_SECRET_FILE}, {API_SERVICE_NAME}, {API_VERSION}, {SCOPES}). {e}")
        Log.error(f"{traceback.format_exc()}")
        return None


def create_service_oauth2(client_secret_file, api_name, api_version, *scopes):
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    cred = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_PATH):
        cred = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_PATH, 'w') as token:
            token.write(cred.to_json())

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        Log.info(API_SERVICE_NAME + ' service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None


def gd_create_folder(folder_name: str, parent_id: str, service):
    file_metadata = {
        'name': folder_name,
        'mimeType': MIME_FOLDER,
        'parents': [parent_id]
    }
    file = service.files().create(body=file_metadata).execute()
    Log.info('Folder created: %s (%s) successfully' % (file.get('name'), file.get('id')))
    return file.get('id')  # return folder id


def gd_create_folder_if_not_exist(folder_name: str, parent_id: str, service):
    folder_id = gd_get_object_id(folder_name, parent_id, service)
    if folder_id is not None:
        return folder_id

    file_metadata = {
        'name': folder_name,
        'mimeType': MIME_FOLDER,
        'parents': [parent_id]
    }
    file = service.files().create(body=file_metadata).execute()
    Log.debug('Folder created: %s (%s) successfully' % (file.get('name'), file.get('id')))
    return file.get('id')  # return folder id


def gd_get_object_id(name: str, parent_id: str, service):
    page_token = None
    try:
        while True:
            response = service.files().list(
                q=f"name = '{name}' and '{parent_id}' in parents and trashed = false",
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageToken=page_token).execute()
            for file in response.get('files', []):
                return file.get('id')
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
    except Exception as e:
        print(e)

    return None


# returns a dict contains dir_name: dir_id
def gd_get_all_sub_folders(parent_id: str, service):
    sub_dirs = {}
    page_token = None
    while True:
        response = service.files().list(
            q=f"mimeType = '{MIME_FOLDER}' and parents = '{parent_id}' and trashed = false",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=page_token).execute()
        for file in response.get('files', []):
            sub_dirs[file.get('name')] = file.get('id')
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return sub_dirs


# returns a dict contains dir_name: dir_id
def gd_get_all_files(parent_id: str, service):
    sub_dirs = {}
    page_token = None
    while True:
        response = service.files().list(
            q=f"mimeType != '{MIME_FOLDER}' and parents = '{parent_id}' and trashed = false",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=page_token).execute()
        for file in response.get('files', []):
            sub_dirs[file.get('name')] = file.get('id')
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return sub_dirs


def gd_upload_file(local_file_path: str, parent_id: str, service):
    if not path_exist(local_file_path):
        Log.error(f"The file {local_file_path} trying to upload doesn't exit!")
        return None
    if '/' in local_file_path:
        filename = local_file_path.split('/')[-1]
    else:
        filename = local_file_path
    file_suffix = filename.split('.')[-1]
    file_metadata = {
        'name': filename,
        'parents': [parent_id]
    }
    if file_suffix not in FILE_GOOGLE_MIME:
        Log.error(f"Unknown file suffix: {file_suffix}. local file path: {local_file_path}")
        return None
    media = MediaFileUpload(local_file_path, mimetype=FILE_GOOGLE_MIME[file_suffix], resumable=True)
    response = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    Log.info(f"{local_file_path} ({response.get('id')}) created successfully.")
    return response.get('id')


def gd_update_file(local_file_path: str, file_id: str, service):
    if not path_exist(local_file_path):
        Log.error(f"The file {local_file_path} trying to upload doesn't exit!")
        return None
    if '/' in local_file_path:
        filename = local_file_path.split('/')[-1]
    else:
        filename = local_file_path
    file_suffix = filename.split('.')[-1]

    file_metadata = {'name': filename, }

    if file_suffix not in FILE_GOOGLE_MIME:
        Log.error(f"Unknown file suffix: {file_suffix}. local file path: {local_file_path}")
        return None

    media = MediaFileUpload(local_file_path, mimetype=FILE_GOOGLE_MIME[file_suffix], resumable=True)

    response = service.files().update(
        fileId=file_id,
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    Log.info(f"{local_file_path} ({response.get('id')}) updated successfully.")
    return response.get('id')


def gd_download_file(local_path: str, gd_file_id: str, service):
    req = service.files().get_media(fileId=gd_file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, req, 8 * 2 ** 20)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    fh.seek(0)
    with open(local_path, 'wb') as f:
        f.write(fh.read())
        f.close()


def gd_download_file_async(local_path: str, gd_file_id: str, service, callback):
    def _gd_download_file():
        gd_download_file(local_path, gd_file_id, service)
        callback()

    thr = threading.Thread(target=_gd_download_file)
    thr.setDaemon(True)
    thr.start()
    return thr


if __name__ == '__main__':
    s = create_service_service_account('res/spot-v2-service-account.json', 'drive', 'v3',
                                       ['https://www.googleapis.com/auth/drive'])
    APP_FOLDER_ID = '18GxXYaFE7QfyUSA7MBITpUC0QSUuGMGs'  # 我的雲端硬碟 -> 異物檢測
    print(gd_get_all_sub_folders(APP_FOLDER_ID, s))
