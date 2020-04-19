#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

"""Learn docopt.

Usage:
  hello.py

"""
from docopt import docopt

if __name__ == '__main__':
  args = docopt(__doc__, version="test")
  print(args)
