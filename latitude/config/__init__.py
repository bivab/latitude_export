import os
import sys
from os.path import expanduser, dirname, join, exists, isdir
from latitude.config.settings import Settings


def setup(config_file=None):
    config = Settings(config_file)
    globals()['config'] = config
