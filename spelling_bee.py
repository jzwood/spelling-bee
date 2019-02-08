#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""generates charset that produce the most anagrams
"""

from words_from_char_set import count, get_words, get_most_frequent_letter
from os import path
import json
import time


def calculate_best_combo(n, has_pinned_letter=False, five_plus_letters=False):
    dir_path = path.dirname(path.realpath(__file__))
    pinned_letter = ''
    best_combo = []
    best_count = 0
    trie_name = 'trie_5' if five_plus_letters else 'trie'
    with open(path.join(dir_path, 'preprocess/charsets/char_combs_{}.json'.format(n)), 'r') as combos_file:
        with open(path.join(dir_path, 'preprocess/trie/{}.json'.format(trie_name)), 'r') as trie_file:
            combos = json.load(combos_file)
            trie = json.load(trie_file)
            start = time.time()
            for combo in combos:
                if has_pinned_letter:
                    words = get_words(trie, combo)
                    ccount, c = get_most_frequent_letter(combo, words)
                    if ccount > best_count:
                        best_combo = combo
                        best_count = ccount
                        pinned_letter = c
                else:
                    wc = count(trie, combo)
                    if wc > best_count:
                        best_count, best_combo = wc, combo
    elapsed = time.time() - start
    chars = '>5' if five_plus_letters else '>1'
    return n, chars, pinned_letter, best_combo, best_count, elapsed


if __name__ == '__main__':
    for n in range(2, 8):
        print(calculate_best_combo(n, True, True))
        print(calculate_best_combo(n, True))
        # print(calculate_best_combo(n))

'''RESULTS
(2, '>5', 'A', ['A', 'N'], 3, 0.004978179931640625)
(2, '>1', 'A', ['A', 'N'], 8, 0.0061130523681640625)
(2, '>1', ['A', 'N'], 8, 0.004193782806396484)
(3, '>5', 'E', ['E', 'S', 'T'], 21, 0.09943175315856934)
(3, '>1', 'E', ['E', 'L', 'S'], 28, 0.11123013496398926)
(3, '>1', ['E', 'L', 'S'], 28, 0.0778360366821289)
(4, '>5', 'E', ['E', 'R', 'S', 'T'], 86, 1.3184523582458496)
(4, '>1', 'E', ['E', 'R', 'S', 'T'], 102, 1.4448139667510986)
(4, '>1', ['E', 'R', 'S', 'T'], 102, 1.0265119075775146)
(5, '>5', 'E', ['A', 'E', 'R', 'S', 'T'], 278, 12.830595016479492)
(5, '>1', 'E', ['A', 'E', 'R', 'S', 'T'], 305, 14.061622142791748)
(5, '>1'. ['A', 'E', 'R', 'S', 'T'], 354, 10.120559930801392)
(6, '>5', 'E', ['A', 'E', 'P', 'R', 'S', 'T'], 566, 89.28628492355347)
(6, '>1', 'E', ['A', 'E', 'P', 'R', 'S', 'T'], 602, 191.60411596298218)
(6, '>1', ['A', 'E', 'P', 'R', 'S', 'T'], 716, 69.02875804901123)
(7, '>5', 'E', ['A', 'E', 'I', 'N', 'R', 'S', 'T'], 1243, 486.240825176239)
(7, '>1', 'E', ['A', 'E', 'I', 'N', 'R', 'S', 'T'], 1284, 511.1471359729767)
(7, '>1', ['A', 'E', 'I', 'N', 'R', 'S', 'T'], 1592, 350.84391593933105)
```
