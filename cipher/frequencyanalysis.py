import re
from itertools import groupby
from collections import Counter, OrderedDict

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
		self.relative_frequency = dict(a_count.most_common())

		# outputs letter frequencies alphabetically (a-z) like {'a': 12, 'b': 5... }
		self.frequency = sorted(self.relative_frequency)

		

		# eventually use dotall to read over \n

		# in a text of "aaaaabbbbaaaaa"
		# for the keys in the dictionary of most common letters, use findall to list 
		# each letter and every letter before it, making a list of lists. [['aa', 'ba'], ['ab', 'bb'], ...]
		# then, reduce the list of lists into a single list. ['aa', 'bb', 'ab', 'bb', ...]
		two_letters = reduce(lambda x, y: x + y, ((re.findall(r'(\w{0})'.format(k), text)) for k,v in self.relative_frequency.items()))	
		
		# for the long list of all two letter pairs, return a Counter object dictionary
		# in the order of largest to smallest. {'aa': 1, 'bb': 2, ...}
		two_letters_dictionary = Counter(two_letters)
		
		# filter the dictionary to return pairs that are unique, i.e. greater than one.
		# like {'bb': 2, ...}
		two_letters_greater_than_one = {k:v for k, v in two_letters_dictionary.items() if v > 1}


		three_letters = reduce(lambda x, y: x + y, ((re.findall(r'(\w{0})'.format(k), text)) for k, v in two_letters_greater_than_one.items()))
		three_letters_dictionary = Counter(three_letters)
		three_letters_greater_than_one = {k:v for k, v in three_letters_dictionary.items() if v > 1}

		snippets_dict = {}
		# while :
		# 	# takes an input dictionary
		# 	snippets = reduce(lambda x, y: x + y, ((re.findall(r'(\w{0})'.format(k), text)) for k,v in input_dictionary.items()))
		# 	snippets_frequency = Counter(snippets)
		# 	nonunique_snippets = {k:v for k, v in snippets.items() if v > 1}
		# 	if nonunique_snippets != {}:
		# 		snippets_dict.update(nonunique_snippets)	
		# 	return nonunique_snippets
		
		# return snippets_dict	
		return two_letters_greater_than_one, three_letters_greater_than_one

class transpositions(object):
	pass 


if __name__ == "__main__":

	text = 'AAAAAAAASDFAWEFADGSRTGREARAGRDGSFGSFDXBCVBDFGFHGJFGHJYUITYUIRYRYUIRTHJKDFGNBNMXCBSDFHJSDFHSSDFBBNMSDFHJSDFTT'

	a_count = analysis(text)


	print(a_count.frequency())

	# print(a_count.snippets())


