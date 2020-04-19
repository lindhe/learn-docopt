#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

"""Learn docopt.

USAGE:
hello.py <input_file> [options]

OPTIONS:
  -b --bar BAR       Sets bar to BAR. [default: asdf]
  -f --foo           Sets foo to true.
  -o --output FILE   Sets output file.
  -h --help          Show this help.
  --version          Print version and exit.

"""

from docopt import docopt

__author__ = "Andreas Lindhé"
__license__ = "MIT"
__version__ = "0.1.0"

if __name__ == '__main__':
  args = docopt(__doc__, version=__version__)
  print(args)
