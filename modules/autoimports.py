import sys
import inspect
import warnings
import types


def import_module(module_name):
    """
    Dynamically imports a module and adds it to the caller's globals.

    Args:
        module_name (str): Name of the module to import.

    Returns:
        module: The imported module.
    """
    module = __import__(module_name)
    try:
        caller_globals = inspect.stack()[1].frame.f_globals
        caller_globals[module_name] = module
    except (TypeError, IndexError):
        pass
    return module


def is_nonstandard_module(module):
    """
    Checks if a module is considered non-standard.

    A module is considered non-standard if it is not part of the standard library
    or a built-in module, or if it is located in a 'site-packages' directory.

    Args:
        module: The module to check.

    Returns:
        bool: True if the module is non-standard, False otherwise.
    """
    stdlib_module_names = getattr(sys, 'stdlib_module_names', ())
    builtin_module_names = sys.builtin_module_names
    is_nonstandard = (
        module.__name__ not in {*stdlib_module_names, *builtin_module_names} or
        any('site-packages' in (getattr(module, attr, None) or '') for attr in ('__file__', '__path__'))
    )
    return is_nonstandard


def warn_nonstandard_module_usage(module):
    """
    Issues a deprecation warning for non-standard module usage.

    Args:
        module: The non-standard module that is being used.
    """
    warning_msg = f"Using non-standard module '{module}' through utils is deprecated."
    warnings.warn(warning_msg, stacklevel=2)


def auto_import_modules(path):
    """
    Auto-imports the specified modules and updates the globals dictionary.

    This function reads the module names from a text file,
    dynamically imports each module, checks if it is non-standard,
    and adds it to the globals dictionary.
    """
    globals_dict = globals()
    globals_dict.update(sys.modules)

    with open(path, 'r') as file:
        module_names = (line.strip() for line in file)

    for module_name in module_names:
        if module_name in globals_dict:
            continue

        module = import_module(module_name)
        if is_nonstandard_module(module):
            warn_nonstandard_module_usage(module)

        globals_dict[module_name] = types.ModuleType(module_name)


auto_import_modules('data/autoimports.txt')
