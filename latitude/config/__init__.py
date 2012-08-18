from latitude.config.settings import Settings


def setup(config_file=None):
    config = Settings(config_file)
    globals()['config'] = config
