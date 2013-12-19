import re
from itertools import groupby
from collections import Counter


class ciphertext(object):
	
	def __init__(self, text):
		self.text = text
		# text = sys.argv[1]

class analysis(object):

	def __init__(self, text):
		self.text = text
		
	def frequency(self):
		# Alphabetical list of (letter, frequency) tuples in text.
		# eventually use super to inherit from class Counter()
		
		a_count = Counter(text)
		# if the letter is not present in the text, it is not listed in the frequency calculations (even as 0)
		
		# outputs largest to smallest frequency {'e': 25, 'a': 12 ...}
		letters_dict = dict(a_count.most_common())

		# outputs letter frequencies alphabetically (a-z) like {'a': 12, 'b': 5... }
		self.frequency = sorted(letters_dict)
	
		snippets_list = []

		# dangerous! rewrite as generator
		while True:
		# eventually use dotall to read over \n

		# in a text of "aaaaabbbbaaaaa"
		# for the keys in the dictionary of most common letters, use findall to list 
		# each letter and every letter before it, making a list of lists. [['aa', 'ba'], ['ab', 'bb'], ...]
		# then, reduce the list of lists into a single list. ['aa', 'bb', 'ab', 'bb', ...]
			snippets = reduce(lambda x, y: x + y, ((re.findall(r'(\w{0})'.format(k), text)) for k,v in letters_dict.items()))
		
		# for the long list of all two letter pairs, return a Counter object dictionary
		# in the order of largest to smallest. {'aa': 1, 'bb': 2, ...}
			snippets_frequency = Counter(snippets)

		
		# filter the dictionary to return pairs that are unique, i.e. greater than one.
		# like {'bb': 2, ...}
			nonunique_snippets = {k:v for k, v in snippets_frequency.items() if v > 1}
			
			if not nonunique_snippets:
				break 
			
			snippets_list.append(nonunique_snippets)
			letters_dict = nonunique_snippets
			
		return snippets_list
		

class transpositions(object):
	pass 


if __name__ == "__main__":

	text = 'AAAAAASDFAWEFASDFADGSRTGREASDFARAGRDASDGSFGSFREWDXBCVBDREWQFGFHREWGJFGHREWQSFHSSDFBBNMSDFHSDFTT'

	a_count = analysis(text)


	print(a_count.frequency())

	# print(a_count.snippets())


