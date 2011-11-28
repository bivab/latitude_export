from client import Latitude
import sys
import gflags

def main(argv):
    print 'main()'
    # Let the gflags module process the command-line arguments
    try:
        argv = gflags.FLAGS(argv)
        print argv
    except gflags.FlagsError, e:
        print '%s\\nUsage: %s ARGS\\n%s' % (e, argv[0], FLAGS)
        sys.exit(1)
    args = {
        'granularity':'best',
        }
    locations = Latitude.location().list(**args).execute()
    import pdb; pdb.set_trace()

main(sys.argv)
