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
		self.relative_frequency = a_count.most_common()
		self.frequency = sorted(self.relative_frequency)
		# return self.frequency, self.relative_frequency
		
	# def snippets(self):
		# Calling set on the list returned by findall removes all the repeated letters.

		two_letters = reduce(lambda x, y: x + y, ((re.findall(r'(\w{0})'.format(pair[0]), text)) for pair in self.relative_frequency))
		# eventually use dotall to read over lines
		
		two_letters_dictionary = dict(Counter(two_letters))
		two_letters_greater_than_one = dict((k, v) for k, v in two_letters_dictionary.items() if v > 1)

		return two_letters_greater_than_one
		

class transpositions(object):
	pass 


if __name__ == "__main__":

	text = 'AAAAAAAASDFAWEFADGSRTGREARAGRDGSFGSFDXBCVBDFGFHGJFGHJYUITYUIRYRYUIRTHJKDFGNBNMXCBSDFHJSDFHSSDFBBNMSDFHJSDFTT'

	a_count = analysis(text)


	print(a_count.frequency())

	# print(a_count.snippets())


