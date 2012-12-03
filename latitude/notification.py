from latitude.config import config
import requests
import json


class task_notification(object):
    def __init__(self, task):
        self.task = task

    def __enter__(self, *args):
        m = self.task.message()
        for n in _notifiers:
            n.send(m, 'Start')

    def __exit__(self, *args):
        m = 'Done'
        for n in _notifiers:
            n.send(m, 'End')


class Notification(object):

    def send(self, message, title=''):
        raise NotImplementedError


class ProwlNotification(Notification):
    name = 'prowl'

    def __init__(self):
        self.setup_prowl()

    def setup_prowl(self):
        import prowlpy
        apikey = config.get('Prowl', 'api_key')
        self.prowl = prowlpy.Prowl(apikey)

    def send(self, message, title=''):
        if title == 'End':
            return  # hack
        self.prowl.add('LatitudeExport', '', message, 1, None)


class PushoverNotification(Notification):
    name = 'pushover'

    def __init__(self):
        self.apitoken = config.get('Pushover', 'api_key')
        self.usertoken = config.get('Pushover', 'user_token')
        self.default_sound = None
        self.error_sound = None
        if config.has_option('Pushover', 'default sound'):
            self.default_sound = config.get('Pushover', 'default sound')
        if config.has_option('Pushover', 'error sound'):
            self.error_sound = config.get('Pushover', 'error sound')
        self.load_sounds()

    def load_sounds(self):
        sounds = {}
        try:
            resp = requests.get('https://api.pushover.net/1/sounds.json')
            if resp.status_code == 200:
                s = json.loads(resp.content)['sounds']
                sounds = dict((v, k) for k, v in s.iteritems())
        except requests.exceptions.RequestException:
            # catch any exception caused by a bad request and ignore it
            pass
        finally:
            self.sounds = sounds

    def send(self, message, title=''):
        payload = {
            "token": self.apitoken,
            "user":  self.usertoken,
            "message": message,
        }
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        if title == 'End':
            return  # hack
        if title == 'Failed' and self.error_sound:
            assert self.error_sound in self.sounds
            payload['sound'] = self.sounds[self.error_sound]
        elif self.default_sound:
            assert self.default_sound in self.sounds
            payload['sound'] = self.sounds[self.default_sound]
        if title != '':
            payload['title'] = title
        resp = requests.post('https://api.pushover.net/1/messages.json',
                        data=payload, headers=headers)
        resp.raise_for_status()


class TerminalNotification(Notification):
    name = 'terminal'

    def send(self, message, title=''):
        print "LatitudeExport: %s" % message

_notifiers = []
for c in [TerminalNotification, ProwlNotification, PushoverNotification]:
    if c.name in config.get('LatitudeExporter', 'notifications'):
        _notifiers.append(c())


def exception_notification(e):
    import traceback
    for n in _notifiers:
        n.send(traceback.format_exc(), 'Failed')
