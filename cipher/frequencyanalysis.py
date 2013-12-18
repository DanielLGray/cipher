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
		self.relative_frequency = a_count.most_common()
		self.frequency = sorted(self.relative_frequency)
		# return self.frequency, self.relative_frequency
		
	# def snippets(self):
		# Calling set on the list returned by findall removes all the repeated letters.

		two_letters = [sorted(set(re.findall(r'(\w{0})'.format(pair[0]), text))) for pair in self.relative_frequency]
		# eventually use dotall to read over lines
		# two_letters_counter = Counter(two_letters)
		# for k, v in groupby(two_letters, key=lambda x: x)

		# Idea : for key, each_list in groupby(two_letters, key=lambda x: x[0]):
		#			for each_pair in each_list:
		# 				something...

		# return two_letters_counter
		return two_letters
		

class transpositions(object):
	pass 


if __name__ == "__main__":

	text = 'AAAAAAAASDFAWEFADGSRTGREARAGRDGSFGSFDXBCVBDFGFHGJFGHJYUITYUIRYRYUIRTHJKDFGNBNMXCBSDFHJSDFHSSDFBBNMSDFHJSDFTT'

	a_count = analysis(text)


	print(a_count.frequency())

	# print(a_count.snippets())


