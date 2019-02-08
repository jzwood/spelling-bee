#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""generates all n letter char sets
"""

from itertools import combinations
from os import path
import json
import string

if __name__ == '__main__':
    dir_path = path.dirname(path.realpath(__file__))
    for choose in range(2, 8):
        combos = combinations(string.ascii_uppercase, choose)
        with open(path.join(dir_path, 'charsets/char_combs_{}.json'.format(choose)), 'w') as outfile:
            json.dump([c for c in combos], outfile)
