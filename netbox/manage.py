#!/usr/bin/env python
import os
import sys
import weakref


# Salva
def my_iter_all_python_module_files():
    # This is a hot path during reloading. Create a stable sorted list of
    # modules based on the module name and pass it to iter_modules_and_files().
    # This ensures cached results are returned in the usual case that modules
    # aren't loaded on the fly.
    # MONKEY PATCH TO SOLVE ERROR WHEN IMPORTING napalm from django https://github.com/CiscoTestAutomation/pyats/issues/120
    from collections.abc import Hashable
    keys = sorted(sys.modules)
    # modules = tuple(m for m in map(sys.modules.__getitem__, keys) if not isinstance(m, weakref.ProxyTypes))
    modules = tuple(m for m in map(sys.modules.__getitem__, keys) if ((not isinstance(m, weakref.ProxyTypes)) and isinstance(m, Hashable)))
    return autoreload.iter_modules_and_files(modules, frozenset(autoreload._error_files))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netbox.settings")

    # Salva: MONKEY PATCHING: napalm import fails with django runserver
    from django.utils import autoreload
    autoreload.iter_all_python_module_files = my_iter_all_python_module_files

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
