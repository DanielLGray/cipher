import re
from itertools import groupby

class ciphertext(object):
	
	def __init__(self, text):
		self.text = text

		# text = sys.argv[1]

class repeats(object):
	pass

class analysis(object):

	def __init__(self, text):
		self.text = text
		self.ALPHABET = [
			'A',
			'B',
			'C',
			'D',
			'E',
			'F',
			'G',
			'H',
			'I',
			'J',
			'K',
			'L',
			'M',
			'N',
			'O',
			'P',
			'Q',
			'R',
			'S',
			'T',
			'U',
			'V',
			'W',
			'X',
			'Y',
			'Z',
		]
		
	def frequency_count(self):
		# Alphabetical list of (letter, frequency) tuples in text.
		self.frequency = [(LETTER, text.count(LETTER)) for LETTER in self.ALPHABET] 
		# Using groupby, dictionary of letter: length of the list of each letter in the sorted text.
		#  self.frequency = {k:len(list(v)) for k,v in groupby(sorted(text))}

		return self.frequency

	def relative_frequency(self):
		# Tuples of (letter, frequency) sorted by most common to least common letter.
		self.relativefrequency = sorted(self.frequency, key=lambda x: x[1], reverse=True)
		print(self.relativefrequency)
		
	def repeats(self):
 		nonzerofrequency = [x for x in self.relativefrequency if x[1] != 0]
 		return True
 		

class transpositions(object):
	pass 


if __name__ == "__main__":

	text = 'AAAAAAAASDFAWEFADGSRTGREARAGRDGSFGSFDXBCVBDFGFHGJFGHJYUITYUIRYTT'

	a_count = analysis(text)

	print(a_count.frequency_count())

	print(a_count.relative_frequency())



