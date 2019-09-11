__author__ = "ResearchInMotion"

from setuptools import setup

#APP would be the name of the file your code is in.
APP = ['main.py']
DATA_FILES = []
#The Magic is in OPTIONS.
OPTIONS = {
    'argv_emulation': False,
    'iconfile': '/Users/sahilnagpal/PycharmProjects/LibraryMS/icons/icon.icns', #change app.icns to the image file name!!!
    }

setup(
    app=APP,
    name='Library Management System', #change to anything
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)