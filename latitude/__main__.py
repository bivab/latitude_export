import gflags
import sys
from datetime import date, timedelta

from latitude.client import Latitude
from latitude.data.json import JSON
from latitude.data.kml import KML
from latitude import config
def main(argv):
    # Let the gflags module process the command-line arguments
    try:
        argv = gflags.FLAGS(argv)
    except gflags.FlagsError, e:
        print '%s\\nUsage: %s ARGS\\n%s' % (e, argv[0], gflags.FLAGS)
        sys.exit(1)
    some_date = date.today() - timedelta(days=1)
    locations = Latitude().locations(some_date)
    exporters = [cls() for cls in config.exporters()]
    formats = config.formats()
    for d in [cls(locations, some_date) for cls in formats]:
        for e in exporters:
            e.write(d)

main(sys.argv)
