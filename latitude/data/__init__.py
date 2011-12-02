class Data(object):
    def __init__(self, data, date):
        self.data = data
        self.date = date

    def prepare(self):
        raise NotImplementedError

    @property
    def extension(self):
        raise NotImplementedError

    def write(self, filename):
        raise NotImplementedError

