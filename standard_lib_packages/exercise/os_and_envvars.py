#!/usr/local/bin/python3

from os import getenv
from math import pi

# optional: 'DIGITS' envvar allows us to set the desired number of digits
digits = int(getenv("DIGITS") or 10)
print("%.*f" % (digits, pi))