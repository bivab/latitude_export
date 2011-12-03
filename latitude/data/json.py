from __future__ import absolute_import
from latitude.data import Data
class JSON(Data):
    extension = 'json'

    def __str__(self):
        json = __import__('json')
        return json.dumps(self.data)
format = JSON
