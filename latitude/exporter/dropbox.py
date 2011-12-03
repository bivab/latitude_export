from latitude.exporter import Exporter
from latitude.config import dropbox as db
from oauth import oauth

class Dropbox(Exporter):
    def __init__(self):
        self.client = db.get_client()

    def write(self, data):
        filename = self.build_filename(data)
        self.client.put_file(filename, str(data), overwrite=True)

    def build_filename(self, data):
        d = data.date
        sep = '/'
        path = "%d%s%d%s%d.%s" % (d.year, sep,
                                    d.month, sep,
                                    d.day, data.extension)
        return path
exporter = Dropbox
