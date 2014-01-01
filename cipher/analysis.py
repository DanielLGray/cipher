import sys
from collections import Counter
from math import trunc
import ignore_characters

"""
This module uses a boxcar method to find repeated patters, (>1 instance) in a text.
Edit the ignore_characters.py configuration file, with lists "automatic" and "user_added"
to add or subtract characters from the analysis (' ', '\ n' and '\ t' ignored by default).

Frequency class: specify filename if run as a stand-alone, or pass text to class instance on import.

Example function calls:

	text = "take me to your leader"
	a_count = Frequency(text)
 	boxcar_freqencies = a_count.boxcar()
	print boxcar_freqencies



"""


class Frequency(object):

	def __init__(self, text, length=3):
		self.text = text
		self.length = length
		self.DEBUG = False
		
	def boxcar(self, length=3):
		"""
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





	def snippets(self):
		pass


# also, mark distances between non-overlapping repeats
# extend counter class to contain information about location... or build your own.

if __name__ == "__main__":
	text = "abcabcabcabcabcabc"
	a_count = Frequency(text)
 	boxcar_freqencies = a_count.boxcar()
	print boxcar_freqencies
