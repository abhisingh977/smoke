import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import storage
from google.oauth2 import service_account

'''
This class manages the Authentication and connection with cloud storages.
'''


class ImageManager():
    '''
    Initialize name
    '''
    def __init__(self):
        self.project = 'affable-beach-268518'
        self.auth = 'auth/affable-beach-268518-0e34b5e46a62.json'
        self.bucket_name = 'smoke_data'
        self.database = 'smoke'

    def bucket(self):
        '''
        Authorization and connection of with cloud bucket
        '''
        with open(self.auth) as source:
            info = json.load(source)
        storage_credentials = service_account.Credentials. \
            from_service_account_info(info)
        storage_client = storage.Client(project=self.project,
                                        credentials=storage_credentials)
        self.bucket_info = storage_client.get_bucket(self.bucket_name)

        return self.bucket_info

    def db(self):
        '''
        Authorization and connection of with cloud firestore
        '''
        cred = credentials.Certificate(self.auth)
        firebase_admin.initialize_app(cred, {
                        'projectId': self.project})
        db = firestore.client()
        self.db_col = db.collection(self.database)
        return self.db_col
