"""Magic functions for InteractiveShell.
"""

#-----------------------------------------------------------------------------
#  Copyright (C) 2001 Janko Hauser <jhauser@zscout.de> and
#  Copyright (C) 2001 Fernando Perez <fperez@colorado.edu>
#  Copyright (C) 2008 The IPython Development Team

#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Our own packages
from IPython.core.magic import Magics, register_magics, line_magic

#-----------------------------------------------------------------------------
# Magic implementation classes
#-----------------------------------------------------------------------------


@register_magics
class DeprecatedMagics(Magics):
    """Magics slated for later removal."""

    @line_magic
    def install_profiles(self, parameter_s=''):
        """%install_profiles has been deprecated."""
        print '\n'.join([
            "%install_profiles has been deprecated.",
            "Use `ipython profile list` to view available profiles.",
            "Requesting a profile with `ipython profile create <name>`",
            "or `ipython --profile=<name>` will start with the bundled",
            "profile of that name if it exists."
        ])

    @line_magic
    def install_default_config(self, parameter_s=''):
        """%install_default_config has been deprecated."""
        print '\n'.join([
            "%install_default_config has been deprecated.",
            "Use `ipython profile create <name>` to initialize a profile",
            "with the default config files.",
            "Add `--reset` to overwrite already existing config files with defaults."
        ])
