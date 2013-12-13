import re

class ciphertext(object):
	
	def __init__(self, text):
		self.text = text

		# text = sys.argv[1]

class repeats(object):
	pass

class frequency(object):

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
		
	def frequency(self, text):
		# Alphabetical list of (letter, frequency) tuples in text.
		self.frequency = [(LETTER, text.count(LETTER)) for LETTER in self.ALPHABET] 
		return self.frequency

	def relative_frequency(self):
		@frequency()
		# Tuples of (letter, frequency) sorted by most common to least common letter.
		self.relativefrequency = sorted(self.frequency, key=lambda x: x[1], reverse=True)
		return self.relativefrequency

	def repeats(self):
 		nonzerofrequency = [x for x in self.relativefrequency if x[1] != 0]

 		

class transpositions(frequency):
	pass 


if __name__ == "__main__":

	text = 'ASDFAWEFADGSRTGREARAGRDGSFGSFDXBCVBDFGFHGJFGHJYUITYUIRYTT'

	a_count = frequency(text)

	# print a_count.frequency, "\n", a_count.relativefrequency

	print a_count.relativefrequency	



