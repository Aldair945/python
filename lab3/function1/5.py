import itertools
def permutations(word):
    word_permts = itertools.permutations(word)
    for perm in word_permts:
        print(''.join(perm))
word = input()
permutations(word)
