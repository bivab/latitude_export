import os
from latitude.config import config
from latitude.exporter import Exporter


class Filesystem(Exporter):
    def __init__(self):
        pass

    def write(self, data):
        path = self.prepare_path(data)
        filename = "%s%s.%s" % (path, data.date.day, data.extension)
        with open(filename, 'w') as f:
            f.write(str(data))

    def prepare_path(self, data):
        d = data.date
        basepath = config.get('Filesystem', 'basepath')
        basepath = os.path.expanduser(basepath)
        sep = os.sep
        path = "%s%s%d%s%d%s" % (basepath, sep, d.year, sep, d.month, sep)
        if not os.path.isdir(path):
            assert not os.path.exists(path)
            os.makedirs(path)
        return path
exporter = Filesystem
