import json
class Data(object):
    def __init__(self, data, date):
        self.data = data
        self.date = date

    def __str__(self):
        raise NotImplementedError

    @property
    def extension(self):
        raise NotImplementedError

class JSON(Data):
    extension = 'json'

    def __str__(self):
        return json.dumps(self.data)

class KML(Data):
    extension = 'kml'

    def __str__(self):
        raise NotImplementedError
