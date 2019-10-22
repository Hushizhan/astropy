# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This subpackage contains utility modules for compatibility with older/newer
versions of python, as well as including some bugfixes for the stdlib that are
important for Astropy.

Note that all public functions in the `astropy.utils.compat.misc` module are
imported here for easier access.

The content of this module is solely for internal use of ``astropy``,
so use it at your own risk.

"""

from .misc import *  # noqa

# Importing this module will also install monkey-patches defined in it
from .numpycompat import *  # noqa
