from datetime import date, timedelta
from latitude import config
from latitude.client import Latitude
from latitude.data.json import JSON
from latitude.data.kml import KML

def dates(start, end, step=None):
    """Generator that yields date objects correspondig to all all steps given
    by step (a timedelta) object. Starting on the date given by start up to the
    date given by end"""

    if step is None:
        step = timedelta(days=1)
    current = start
    while current < end:
        yield current
        current += step

class Importer(object):
    exporters = [cls() for cls in config.exporters()]
    formats = config.formats()

class BatchImporter(Importer):
    """Import all google latitude information
    on a day by day basis starting at
    a given day up to the current date"""
    def __init__(self, date):
        self.start_date = self.parse_date(date)

    def parse_date(self, d):
        d = [int(_) for _ in d.split('/')]
        assert len(d) == 3
        return date(d[0], d[1], d[2])

    def run(self):
        for some_date in dates(self.start_date, date.today()):
            locations = Latitude().locations(some_date)
            for d in [cls(locations, some_date) for cls in self.formats]:
                for e in self.exporters:
                    e.write(d)

class YesterdayImporter(Importer):
    """Import the Google latitude location information
    for the previous day and"""

    def run(self):
        some_date = date.today() - timedelta(days=1)
        locations = Latitude().locations(some_date)
        for d in [cls(locations, some_date) for cls in self.formats]:
            for e in self.exporters:
                e.write(d)

