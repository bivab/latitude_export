import apiclient.discovery
import httplib2
import pickle
import os
from apiclient.discovery import build
from apiclient.ext.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
from latitude.config import config


def get_storage_path():
    storage = config.get('OAuth', 'storage')
    dirname = os.path.dirname(os.path.realpath(__file__))
    storage_path = os.path.join(dirname, '..', storage)
    return storage_path

storage = Storage(get_storage_path())
credentials = storage.get()
if credentials is None or credentials.invalid == True:
    flow = OAuth2WebServerFlow(
        client_id=config.get('OAuth', 'client_id'),
        client_secret=config.get('OAuth','client_secret'),
        scope=config.get('OAuth','scope'),
        user_agent=config.get('OAuth','user_agent'))
    credentials = run(flow, storage)

http = httplib2.Http()
http = credentials.authorize(http)

def build(*args):
    global http
    return apiclient.discovery.build(*args, http=http)
