from __future__ import absolute_import
from dropbox import client, session
from latitude.config import config

import json
import os

APP_KEY = config.get('Dropbox', 'app_key')
APP_SECRET = config.get('Dropbox', 'app_secret')
ACCESS_TYPE = config.get('Dropbox', 'access_type')


def get_client():
    sess = get_session()
    return client.DropboxClient(sess)


def load_stored_token():
    path = config.get_storage_path(config.get('Dropbox', 'storage'))
    if not os.path.isfile(path):
        return
    with open(path, 'r') as f:
        token = json.loads(f.read())
    return token


def store_token(token):
    data = {'key': token.key, 'secret': token.secret}
    path = config.get_storage_path(config.get('Dropbox', 'storage'))

    with open(path, 'w') as f:
        f.write(json.dumps(data))


def get_session():
    sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
    token_data = load_stored_token()
    if token_data is None:
        request_token = sess.obtain_request_token()
        url = sess.build_authorize_url(request_token)
        print "url:", url
        print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
        raw_input()
        # This will fail if the user didn't visit the above URL and hit 'Allow'
        access_token = sess.obtain_access_token(request_token)
        store_token(access_token)
    else:
        sess.set_token(token_data['key'],
                            token_data['secret'])

    return sess
