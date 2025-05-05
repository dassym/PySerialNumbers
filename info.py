import sys, os.path
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'src'))

import datetime as DT
import re as RE

from serialnumbers._version import __version__, __ver__, VERSION, DATE, REQUIRED_PYTHON   #@UnusedImport

PUBLISHER = 'Dassym'
SHORTNAME = 'PySerialNumbers'
COMPANY = 'Dassym SA'
COMPANYSHORT = 'dassym'
AUTHORS = ('Fabrice Voillat')

COMPACTNAME = SHORTNAME.lower()

DESCRIPTION = '''The PySerialNumbers library offers functionalities for manipulating serial numbers.'''

def setReleaseDate(isodate):
    d = DT.datetime.strptime(isodate, '%Y-%m-%d')
    ds = '{0:d}, {1:d}, {2:d}'.format(*d.timetuple())
    fname = os.path.join('src','serialnumbers','_version.py')
    with open(fname, 'r+') as f:
        tmp = f.read()
    tmp = RE.sub( r'^DATE\s*=\s*DT\.date\([^)]+\)\s*$',
            "DATE = DT.date({0:s})".format(ds),
            tmp, flags=RE.MULTILINE
            )
    with open(fname, 'w+') as f:
        f.write(tmp)