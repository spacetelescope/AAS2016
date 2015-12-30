"""
Check for required and optional dependencies for the 2016 AAS Astropy
tutorial.

- astropy: 1.0.6 or later required
- numpy: required (version depends on astropy version)
- scipy: required
- matplotlib: required
- photutils: required
- bs4 (BeautifulSoup): optional

Usage::

  % python check_env.py
"""

warnings = False
errors = False

try:
    import astropy
except ImportError as err:
    print('Error: Failed import: {0}'.format(err))
    errors = True
else:
    # Astropy version 1.0.6
    astropy_version = astropy.__version__
    if astropy_version < '1.0.6':
        print('Error: astropy version 1.0.6 or later is required, you have {0}'
              .format(astropy.__version__))
        errors = True

try:
    import numpy
except ImportError as err:
    print('Error: Failed import: {0}'.format(err))
    errors = True

try:
    import scipy
except ImportError as err:
    print('Error: Failed import: {0}'.format(err))
    errors = True

try:
    import matplotlib
except ImportError as err:
    print('Error: Failed import: {0}'.format(err))
    errors = True

try:
    import photutils
except ImportError as err:
    print('Error: Failed import: {0}'.format(err))
    errors = True

try:
    import pandas
except ImportError as err:
    print('Error: Failed import: {0}'.format(err))
    errors = True

# BeautifulSoup4 for one bit of the ASCII tables section.
try:
    import bs4
except ImportError:
    print('Warning: BeautifulSoup4 is not installed, so you will not be '
          'able to run the example for reading HTML tables.')
    warnings = True

print('\nAstropy tutorial environment check summary:')
if errors:
    print('  There are errors that you must resolve before running the '
          'tutorial.')
if warnings:
    print('  There are warnings and some parts of the tutorial will not '
          'work.')
if not errors and not warnings:
    print('  Your Python environment is good to go!')
