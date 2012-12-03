# Latitude Export
This tool downloads and stores the Google latitude location history.

Starting the application downloads the Google latitude data for the previous
day. Its intended use is to create a backup of your Google latitude data.

Currently data can be exported as kml and json and it can be stored on the
local filesystem or in your Dropbox (without creating a local copy).

The success or failure of the process can be sent to the command-line and to
push-notification services, currently Pushover and Prowl.

## Running

python latitude [options]

The default mode imports all Google latitude locations for the previous day.

### Batch import

To import all previous data run python latitude --import YYYY/MM/DD with the
date from which you want to start importing your data.

## Dependencies:
  see requirements.txt for a detailed list of dependencies and versions.

## Setup:
Configuration is stored in an ini-style file. See settings.ini.default for the
details.

You need to register the application with Google, and Dropbox in case you want
to export to Dropbox, the corresponding key and secrets for the applications go
in the settings.ini file.
To register with google visit https://code.google.com/apis/console/b/0 and
create the credentials for the Latitude API.

To register with Dropbox visit https://www.dropbox.com/developers/apps and
create a new app.


## Configuration:
Besides the application information for Google and Dropbox there are several
details that can be configured

### KML
Configuration for the kml export.

* timezone = the timezone to which the timestamps are transformed for the kml
export

### Filesystem

Configuration for the filesystem export
* basepath = is the directory where the Google latitude data should be stored.

The data is stored in the format YYYY/mm/dd.format in the directory given by
basepath.

### LatitudeExporter


#### Global settings

* datadir = directory where the application can store its own data
* formats = formats in which the data should be stored (available: kml, json). Comma separated list
* exporters = exporters that should be used for the data (available: filesystem, dropbox)
* notifications = notifications to be sent (available: prowl and terminal)

### Pushover
Push notifications using the pushover.net service. You need an account on
http://pushover.net. You also need to register a new application in your account.

#### Settings
* api\_key = your api key for the application
* user\_token = your pushover user token
* default sound = (optional) the sound to play
* error sound = (optional) the error sound to play


### Prowl
* api\_key = api key for prowl notifications, see https://www.prowlapp.com/api_settings.php for details.
