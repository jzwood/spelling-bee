# SPELLING BEE
**Rules**: Given 7 letters (including 1 special letter) find as many words* as you can that

    a) include the special letter
    b) do not include any letter that is not one of the 7 letters
    c) are at least 5 characters long

**Question**:
Which 7 letters yield the most words given the above rules?

## Programmatic Approach

```shell
# preprocessing
$ python preprocess/generate_trie.py
$ python preprocess/brute_char_sets.py

# main
$ python spelling_bee.py
```

## Results
The letters that generate the most anagrams are
`A, E, I, N, R, S, T` where `E` is pinned. This generates 1243 (5+ letter)  anagrams.


\* dictionary-legitimate, English, words
