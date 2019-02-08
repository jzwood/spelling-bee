#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""counts all possible anagrams of a given charset
"""

import json
from functools import reduce
import operator


def get_words(trie, charset, partial_word=''):
    keys = set(charset) & (trie.keys())
    if len(keys) is 0:
        return []
    else:
        def get_words_subtrie(key, charset, partial_word):
            subtrie = trie.get(key)
            pword = ''.join([partial_word, key])
            word = [pword] if subtrie.get('#', 0) else []
            return word + get_words(subtrie, charset, pword)
        subwords = [get_words_subtrie(k, charset, partial_word) for k in list(keys)]
        return reduce(operator.concat, subwords)


def count(trie, charset):
    keys = set(charset) & (trie.keys())
    if len(keys) is 0:
        return 0
    else:
        def count_subtrie(key):
            subtrie = trie.get(key)
            return subtrie.get('#', 0) + count(subtrie, charset)
        return sum(map(count_subtrie, list(keys)))


def get_most_frequent_letter(char_set, word_list):
    char_count = {}
    for word in word_list:
        for char in list(set(word)):
            char_count[char] = char_count.get(char, 0) + 1
    max = 0
    max_char = ''
    for char, count in char_count.items():
        if count > max:
            max = count
            max_char = char
    return max, max_char


if __name__ == '__main__':

    json_data = {"b": {"a": {"n": {"a": {"n": {"a": {"#": 1}}}, "d": {"#": 1}, "#": 1}}, "l": {"a": {"n": {"d": {"#": 1}}}}}, "n": {"a": {"b": {"#": 1}}}, "a": {"n": {"b": {"l": {"e": {"#": 1}}}, "#": 1}, "a": {"#": 1}}}

# ['banana','band','nab','anble','bland','aa','an','ban']
    c = count(json_data, "ban")
    assert c is 5

    ws = get_words(json_data, "ban")
    assert sorted(ws) == ['aa', 'an', 'ban', 'banana', 'nab']

    json_data = {"s": {"e": {"t": {"#": 1}}, "t": {"e": {"m": {"#": 1}}, "y": {"#": 1}}}, "t": {"e": {"s": {"t": {"#": 1, "y": {"#": 1}, "s": {"#": 1}}}}}, "e": {"s": {"y": {"#": 1}}}, "l": {"e": {"s": {"t": {"#": 1}}}}}

# ['set','test','testy','stem','esy','sty','lest','tests']
    c = count(json_data, "teys")
    assert c is 6

    ws = get_words(json_data, "teys")
    assert sorted(ws) == ['esy', 'set', 'sty', 'test', 'tests', 'testy']

    # test get_most_frequent_letter
    words = ['CAT', 'CAST', 'SAT', 'AA', 'CATS']
    chars = ('C', 'A', 'S', 'T')
    m, mc = get_most_frequent_letter(chars, words)
    assert m is 5 and mc is 'A'

    words = ['NO', 'NOON', 'OH', 'HOO', 'HMM', 'MOO']
    chars = ('N', 'O', 'H', 'M')
    m, mc = get_most_frequent_letter(chars, words)
    assert m is 5 and mc is 'O'
    print('PASSES TESTS')
