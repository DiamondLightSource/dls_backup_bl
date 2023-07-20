import os
from dls_backup_bl.backup import BackupBeamline


def load_version():
    '''Load version from file and set as __version__ attribute.'''
    package_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(package_dir, 'VERSION')
    with open(filename) as f:
        return f.read().strip()


__version__ = load_version()