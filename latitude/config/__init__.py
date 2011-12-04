import ConfigParser
import os
SETTINGS = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'settings.ini'))

config = ConfigParser.ConfigParser()
config.read(SETTINGS)

# create datadir
datadir = config.get('LatitudeExporter', 'datadir')
datadir = os.path.expanduser(datadir)
if not os.path.exists(datadir):
    os.makedirs(datadir)
assert os.path.isdir(datadir)

def exporters():
    exporters = config.get('LatitudeExporter', 'exporters')
    exporters = [x.strip() for x in exporters.split(',')]
    return [__import__('latitude.exporter.%s' % e, {}, {}, ['exporter']).exporter
                                            for e in exporters]
def formats():
    formats = config.get('LatitudeExporter', 'formats')
    formats = [x.strip() for x in formats.split(',')]
    return [__import__('latitude.data.%s' % f, {}, {}, ['format']).format
                                            for f in formats]

def get_storage_path(storage):
    dirname = datadir
    storage_path = os.path.join(dirname, storage)
    return storage_path

