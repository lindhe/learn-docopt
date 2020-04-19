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
{sys.argv[0]} <input_file> ... [-v | -vv | -vvv] [options]
{sys.argv[0]} --required [--either | --or] [options]

ARGUMENTS:
  <input_file>      Input file.

OPTIONS:
  -b --bar BAR       Sets bar to BAR. [default: asdf]
  --dynamic DYN      This is set dynamically. [default: {dyn}]
  -e --either        Something.
  -f --foo FOO       Sets foo.
  -h --help          Show this help.
  --license          Prints license and exit.
  -o --or            Something else.
  -r --required      This option is required for no reason.
  -v --verbose       Talk more.
  --version          Print version and exit.

"""

if __name__ == '__main__':
  args = docopt(docs, version=__version__)
  print(args)
