#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""generates charset that produce the most anagrams
"""

from words_from_char_set import count, get_words
from os import path
import json
import time
import pprint

if __name__ == '__main__':
    dir_path = path.dirname(path.realpath(__file__))
    with open(path.join(dir_path, 'preprocess/trie/trie_5.json'), 'r') as trie_file:
        trie = json.load(trie_file)
        words = [w for w in get_words(trie, ['A', 'E', 'I', 'N', 'R', 'S', 'T']) if 'E' in set(w)]
        pprint.pprint(words)
        print(len(words))
