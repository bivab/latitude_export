from datetime import datetime
import time

from latitude.config.gdata import setup as gdata_setup, build


class Latitude(object):
    _service = None

    def __init__(self):
        if Latitude._service is None:
            gdata_setup()
            Latitude._service = build("latitude", "v1")

    def locations(self, date, options=None):
        args = self.build_args(date, options)
        loc = Latitude._service.location().list(**args)
        return loc.execute()

    def build_args(self, date, options=None):
        timetuple = date.timetuple()
        start_time = time.mktime(timetuple) * 1000
        end_datetime = datetime(date.year, date.month, date.day, 23, 59)
        end_time = time.mktime(end_datetime.timetuple()) * 1000
        # according to argmap, define at runtime in discovery.py in apiclient
        args = {
            'granularity': 'best',
            'min_time': int(start_time),
            'max_time': int(end_time),
        }
        return args
