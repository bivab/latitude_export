from latitude.config import config

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
        if title == 'End': return
        self.prowl.add('LatitudeExport', '', message, 1, None)



class TerminalNotification(Notification):
    name = 'terminal'

    def send(self, message, title=''):
        print "LatitudeExport: %s" % message

_notifiers = []
for c in [TerminalNotification, ProwlNotification]:
    if c.name in config.get('LatitudeExporter', 'notifications'):
       _notifiers.append(c())
