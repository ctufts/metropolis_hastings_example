try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Traveling Politician - the Clay Davis Edition',
    'author': 'Chris Tufts',
    'url': '',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose','scipy'],
    'packages': ['claydavis'],
    'scripts': [],
    'name': 'claydavis'
}

setup(**config)
