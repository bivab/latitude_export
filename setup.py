from setuptools import setup, find_packages
from latitude import version
from os.path import join, dirname

requirements = open(join(dirname(__file__), 'requirements.txt')).readlines(),
description = open(join(dirname(__file__), 'README.markdown')).read()

setup(
    name=version.__title__,
    version=version.__version__,
    packages=find_packages(),
    long_description=description,
    entry_points={
        'console_scripts': ['latitude = latitude.__main__:entry_point']
    },
    install_requires=requirements,
    )
