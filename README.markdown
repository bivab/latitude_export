# Latitude Export
This tool downloads and stores the Google latitude location history on a
daily basis. Starting the application downloads the Google latitude data for the previous day. Its intended use is to create a backup of your Google latitude data.
Currently data can be exported as kml and json and it can be stored on the
local filesystem or in your Dropbox (without creating a local copy).

## Running

python latitude [options]
or ./latitude.sh [options]

The default mode imports all Google latitude locations for the previous day.
Modify latitude.sh to run in a virtualenv or set some default configuration options.

### Batch import

To import all previous data run python latitude --import YYYY/MM/DD with the
date from which you want to start importing your data

## Dependencies:
* dropbox - Dropbox python SDK (https://www.dropbox.com/developers/reference/sdk)
* google-api-python-client
* python-gflags
* pytz
* prowlpy (https://github.com/jacobb/prowlpy) - only if you want prowl notifications

## Setup:
You need to register the application at Google, and Dropbox in case you want to export
to Dropbox, the corresponding key and secrets for the applications go in
latitude/settings.inc.

## Configuration:
Besides the application information for Google and Dropbox there are several
details that can be configured

### KML
Configuration for the kml export.

timezone = the timezone to which the timestamps are transformed for the kml
export

### Filesystem
Configuration for the filesystem export
basepath = is the directory where the Google latitude data should be stored.
The data is stored in the format YYYY/mm/dd.format in the directory given by
basepath.

###LatitudeExporter
Global settings

datadir = directory where the application can store its own data
formats = formats in which the data should be stored (available: kml, json). Comma separated list
exporters = exporters that should be used for the data (available: filesystem, dropbox)
notifications = notifications to be sent (available: prowl and terminal)

### Prowl
api_key = api key for prowl notifications, see https://www.prowlapp.com/api_settings.php for details.
