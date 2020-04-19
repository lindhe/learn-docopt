#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

import sys
from docopt import docopt

__author__ = "Andreas Lindhé"
__license__ = "MIT"
__version__ = "0.1.0"

dyn = "xkcd"

docs = f"""Learn docopt.

USAGE:
{sys.argv[0]} <input_file> [--either | --or] [options]

OPTIONS:
  -b --bar BAR       Sets bar to BAR. [default: asdf]
  --dynamic DYN      This is set dynamically. [default: {dyn}]
  -e --either        Something.
  -f --foo           Sets foo to true.
  --license          Prints license and exit.
  -o --or            Something else.
  -h --help          Show this help.
  --version          Print version and exit.

"""

if __name__ == '__main__':
  args = docopt(docs, version=__version__)
  print(args)
