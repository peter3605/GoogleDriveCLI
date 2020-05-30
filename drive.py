from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

class DriveObj:
    def __init__(self):
        self.creds = None
        self.service = None
        self.current_folder = None

    """
    Logs into to the user's account using the key stored in credentials.json
    """
    def login(self):
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('drive', 'v3', credentials=self.creds)
        print("Login was a success - current folder is: " )
    
    """
    Prints the names of files in the current directory
    """
    def view_filenames(self, args):
        n = 10
        if '-n' in args.keys():
            n = args['-n']
        results = self.service.files().list(
        pageSize=n, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(item['name'])

    """
    Prints the names of folders in the current directory
    """
    def view_foldernames(self):
        results = self.service.files().list(q="mimeType='application/vnd.google-apps.folder'", fields="nextPageToken, files(id, name)", pageSize=10).execute()
        items = results.get('files', [])
        if not items:
            print('No folders found.')
        else:
            print('Folders:')
            for item in items:
                print(item['name'])
