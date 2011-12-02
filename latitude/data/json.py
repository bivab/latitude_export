from __future__ import absolute_import
from latitude.data import Data
class JSON(Data):
    extension = 'json'

    def prepare(self):
        json = __import__('json')
        return json.dumps(self.data)

    def write(self, filename):
        with open(filename, 'w') as f:
            f.write(self.prepare())
