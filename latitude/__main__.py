import gflags
import sys
from datetime import date, timedelta

from latitude.client import Latitude
from latitude.data import JSON
from latitude.exporter.filesystem import FileSystem

gflags.DEFINE_boolean('debug', False, 'produces debugging output')

def main(argv):
    print 'main()'
    # Let the gflags module process the command-line arguments
    try:
        argv = gflags.FLAGS(argv)
        print argv
    except gflags.FlagsError, e:
        print '%s\\nUsage: %s ARGS\\n%s' % (e, argv[0], gflags.FLAGS)
        sys.exit(1)
    some_date = date.today() - timedelta(days=1)
    locations = Latitude().locations(some_date)
    #.location().list(**args)
    json = JSON(locations, some_date)
    #kml = KML(locations)
    FileSystem().write(json)

    if gflags.FLAGS.debug:
        import pdb; pdb.set_trace()

main(sys.argv)
