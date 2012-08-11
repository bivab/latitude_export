from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='latitude',
    version='1.3',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.markdown')).read(),
    entry_points={
        'console_scripts': ['latitude = latitude.__main__:entry_point']
    },
    install_requires=['urllib3', 'apiclient',
                'gdata', 'google-api-python-client',
                'pytz', 'dropbox'],

    )
