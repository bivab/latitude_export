import gflags
import sys
from latitude.importer import BatchImporter, YesterdayImporter
from latitude.notification import task_notification

# Define command line flags
gflags.DEFINE_string('import',
                    None,
                    'Import past data, provide date as YYYY/MM/DD',
                    short_name='i')

def main(argv):
    # Let the gflags module process the command-line arguments
    try:
        argv = gflags.FLAGS(argv)
    except gflags.FlagsError, e:
        print '%s\nUsage: %s ARGS\n%s' % (e, argv[0], gflags.FLAGS)
        sys.exit(1)
    if getattr(gflags.FLAGS, 'import') is not None:
        date = gflags.FLAGS['import'].value
        task = BatchImporter(date)
    else:
        task = YesterdayImporter()
    with task_notification(task) as _:
        task.run()
main(sys.argv)
