import os
import re
from setuptools import setup

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def read(fname):
    dname = os.path.dirname(__file__)
    fname = os.path.join(dname, fname)

    with open(fname) as f:
        contents = f.read()
        sanatized = cleanhtml(contents)

        try:
            from m2r import M2R
            m2r = M2R()
            return m2r(sanatized)
        except:
            return sanatized

setup(
    name = "pushfin",
    version = "0.2.0",
    author = "Steffen Vogel",
    author_email = "post@steffenvogel.de",
    description = "Publishes bank account transactions and balances via MQTT, Telegram and Pushover.",
    license = "GPL-3.0",
    keywords = "HBCI FinTS Pushover MQTT Telegram",
    url = "https://github.com/stv0g/pushfin",
    long_description = read('README.md'),
    scripts=[
	    'bin/pushfin'
    ],
    setup_requires = [
        'm2r',
    ],
    install_requires = [
	'pyyaml',
	'fints',
	'paho-mqtt'
    ],
    zip_safe = False,
    classifiers = [
	"Development Status :: 5 - Production/Stable",
	"Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.7",
	"Topic :: Office/Business :: Financial",
	"Topic :: Home Automation",
	"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ]
)
