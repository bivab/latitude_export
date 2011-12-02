import gflags
import sys
from datetime import date, timedelta

from latitude.client import Latitude
from latitude.data.json import JSON
from latitude.data.kml import KML
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
    for d in [cls(locations, some_date) for cls in [JSON, KML]]:
        FileSystem().write(d)

    if gflags.FLAGS.debug:
        import pdb; pdb.set_trace()

main(sys.argv)
