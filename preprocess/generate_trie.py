#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""generates trie for scrabble dictionary
"""

import json
from os import path


def add_word_to_trie(trie, word):
    head, tail = word[:1], word[1:]
    subtrie = trie[head] if trie.get(head) is not None else {}
    if tail:
        trie[head] = add_word_to_trie(subtrie, tail)
    elif head:
        subtrie['#'] = 1
        trie[head] = subtrie
    return trie


if __name__ == '__main__':
    dir_path = path.dirname(path.realpath(__file__))
    trie_data = {}
    trie_data_5 = {}
    with open(path.join(dir_path, 'scrabble.txt'), 'r') as dict:
        for word in dict:
            trie_data = add_word_to_trie(trie_data, word.strip())
            if len(word) >= 5:
                trie_data_5 = add_word_to_trie(trie_data_5, word.strip())

    with open(path.join(dir_path, 'trie/trie.json'), 'w') as outfile:
        json.dump(trie_data, outfile)

    with open(path.join(dir_path, 'trie/trie_5.json'), 'w') as outfile:
        json.dump(trie_data_5, outfile)
