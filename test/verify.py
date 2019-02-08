#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""generates trie for scrabble dictionary
"""


def verify(n, chars, anagrams, _):
    count = 0
    with open('preprocess/scrabble.txt', 'r') as dict:
        for word in dict:
            word = word.strip()
            if set(chars) >= set(word):
                count += 1
    result = ("PASSES" if count == anagrams else "FAILED") + "\t{}\t{}".format(count, anagrams)
    return result


results = [(2, ['A', 'N'], 8, 0.004193782806396484),
           (3, ['E', 'L', 'S'], 28, 0.0778360366821289),
           (4, ['E', 'R', 'S', 'T'], 102, 1.0265119075775146),
           (5, ['A', 'E', 'R', 'S', 'T'], 354, 10.120559930801392),
           (6, ['A', 'E', 'P', 'R', 'S', 'T'], 716, 69.02875804901123),
           (7, ['A', 'E', 'I', 'N', 'R', 'S', 'T'], 1592, 350.84391593933105)]

for result in results:
    print(verify(*result))
