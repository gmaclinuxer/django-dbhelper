# -*- coding: utf-8 -*-
VERSION = (0, 1, 0)


def get_version():
    """Return the version as a human-format string."""
    return '.'.join([str(i) for i in VERSION])


__version__ = get_version()
