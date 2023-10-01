
# This is a dummy module to test the import of external modules

# ImportError: attempted relative import with no known parent package
# SHARED_MODULES.shared_data as shared_data

# from ..SHARED_MODULES import shared_data

# add parent folder to sys.path
import sys, os
# sys.path.append('..') # method 1
# sys.path.append(os.path.abspath('..')) # method 2
# sys.path.append(os.pardir) # method 3
from SHARED_MODULES import shared_data


def print_dummies():
    print("D U M M I E S")
    shared_data.print_value()

