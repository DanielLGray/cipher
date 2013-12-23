import re
from collections import Counter
import ignore_characters



class ciphertext(object):
	
	def __init__(self, text):
		self.text = text
		# text = sys.argv[1]

class Frequency(object):


	def __init__(self, text, length=3):
		self.text = text
		self.length = length
		
	def no_overlaps(self):
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
# use permutations to search though document? Faster?
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
		

	def overlaps(self, length=3):
		"""
		This module uses a boxcar method to find repeated patters, (>1 instance) in a text.
		Edit the ignore_characters.py configuration file, with lists "automatic" and "user_added"
		to add or subtract characters from the analysis (' ', '\ n' and '\ t' ignored by default).
		
		Frequency class: specify filename if run as a stand-alone, or pass text to class instance on import.
		
		Example function calls:

			text = "take me to your leader"
			text_analysis = Frequency(text)
 			print text_analysis.overlaps()
			
		Use self.length to set the minimum pattern length. The default pattern length is 3, like [('abc',2), ('bca')....] in 'abcabcabc'. 		
		Use re.findall if you are looking for non-overlapping patterns.
		"""
		
		ignored_text = ignore_characters.automatic + ignore_characters.user_added
		ignore_this_letter = False
		self.combinations = Counter()
		last_boxcar = len(text) - length + 1
		for start_letter in range(0, last_boxcar):		
			if text[start_letter] in ignored_text:
				break
			for expansion in range(0, (len(text)-length-start_letter)+1):
				end_letter = start_letter + length + expansion
				text_slice = text[start_letter:end_letter]
				for letter in text_slice:
					if letter in ignored_text:
						ignore_this_letter = True
						break
				if ignore_this_letter:
					break
				left_slice = text[:(start_letter+len(text_slice)-1)]
				right_slice = text[(start_letter+1):]
				if text_slice in left_slice or text_slice in right_slice:
					text_slice_list = [text_slice]
					self.combinations.update(text_slice_list)
		return self.combinations




# also, mark distances between non-overlapping repeats
# extend counter class to contain information about location... or build your own.

if __name__ == "__main__":

	# with open('hamlet.txt', 'r') as f:
	# 	text = f.read()
	# 	a_count = analysis(text)
	# 	print(a_count.frequency())


	text = "abcabc"
	text_analysis = Frequency(text)
 	print "text is:", text
 	print text_analysis.no_overlaps()
 	print text_analysis.overlaps()

