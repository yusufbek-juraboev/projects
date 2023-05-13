import pandas as pd
from itertools import combinations, permutations


def angram_word(entered_word):
	anagrams = []
	word_list = pd.read_csv("4000.csv")
	perm = permutations(list(entered_word), len(list(entered_word)))
	for j in perm:
		s = ''.join(j)
		for k in word_list['words'].values:
			if s == k:
				anagrams.append(s)
	return anagrams


word = input("Write a word: ")
anagram = angram_word(word)
print(anagram)
