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
		# use super to inherit from class Counter()
		a_count = Counter(text)
		self.relative_frequency = a_count.most_common()
		self.frequency = sorted(self.relative_frequency)
		return self.frequency, self.relative_frequency
		
	def snippets(self):
		# Calling set on the list returned by findall removes all the repeated letters.
		two_letters = [(pair[0], set(re.findall(r'(\w)' + pair[0], text))) for pair in self.relative_frequency]
		return two_letters

class transpositions(object):
	pass 


if __name__ == "__main__":

	text = 'AAAAAAAASDFAWEFADGSRTGREARAGRDGSFGSFDXBCVBDFGFHGJFGHJYUITYUIRYTT'

	a_count = analysis(text)


	print(a_count.frequency())

	print(a_count.snippets())


