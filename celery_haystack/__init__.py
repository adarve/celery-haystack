__version__ = '0.11'


def version_hook(config):
    config['metadata']['version'] = __version__
