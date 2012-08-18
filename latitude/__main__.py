import gflags
import sys

# Define command line flags
gflags.DEFINE_string('import',
                    None,
                    'Import past data, provide date as YYYY/MM/DD',
                    short_name='i')
# Define command line flags
gflags.DEFINE_string('config',
                    None,
                    'Configuration file',
                    short_name='c')


def setup_config():
    from latitude import config
    if getattr(gflags.FLAGS, 'config') is not None:
        config_file = gflags.FLAGS['config'].value
        config.setup(config_file)
    else:
        config.setup()


def run():
    from latitude.importer import BatchImporter, YesterdayImporter
    from latitude.notification import task_notification

    if getattr(gflags.FLAGS, 'import') is not None:
        date = gflags.FLAGS['import'].value
        task = BatchImporter(date)
    else:
        task = YesterdayImporter()
    with task_notification(task):
        task.run()


def main(argv):
    # Let the gflags module process the command-line arguments
    try:
        argv = gflags.FLAGS(argv)
    except gflags.FlagsError, e:
        print '%s\nUsage: %s ARGS\n%s' % (e, argv[0], gflags.FLAGS)
        sys.exit(1)

    setup_config()
    run()


def entry_point():
    try:
        main(sys.argv)
    except Exception, e:
        from latitude.notification import exception_notification
        exception_notification(e)
        raise

if __name__ == '__main__':
    main(sys.argv)
