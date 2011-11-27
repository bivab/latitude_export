from client import Latitude
import sys
import gflags

def main(argv):
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
    print Latitude.location().list(**args).execute()

if __name__ == '__main__':
    main(sys.argv)
