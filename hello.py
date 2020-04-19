#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

import sys
from docopt import docopt

dyn = "xkcd"

docs = f"""Learn docopt.

USAGE:
{sys.argv[0]} <input_file> [options]

OPTIONS:
  -b --bar BAR       Sets bar to BAR. [default: asdf]
  --dynamic DYN      This is set dynamically. [default: {dyn}]
  -f --foo           Sets foo to true.
  -o --output FILE   Sets output file.
  -h --help          Show this help.
  --version          Print version and exit.

"""

__author__ = "Andreas Lindhé"
__license__ = "MIT"
__version__ = "0.1.0"

if __name__ == '__main__':
  args = docopt(docs, version=__version__)
  print(args)
