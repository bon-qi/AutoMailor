import sys
from setuptools import setup, find_packages
#from version import __version__

setup(
    name = 'automailor',
    packages = find_packages(),
    version = '0.0.0', 
    description = 'automailor, a monitor for daily research',
    license = 'MIT',
    author = 'Qi Zhang',
    author_email = 'qi-001@outlook.com',
    keywords = [
        'spider',
        'academic research'
    ],
    data_files = [
        "./automailor/config/config_url.json",
        "./automailor/config/config_send.json"
    ],
    install_requires = [
      'requests',
    ]
)
