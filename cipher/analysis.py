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
		self.combinations = Counter()
		end_of_text = False

		if self.DEBUG:
			print "length of text:", len(text)
			print "length of boxcar", length

		last_boxcar = len(text) - length + 1
		if self.DEBUG:
			print "last_boxcar =", last_boxcar

		for start_letter in range(0, last_boxcar):		
			if self.DEBUG:
				print "\n-----------\ntext[",start_letter, "] range", range(0, last_boxcar), \
				"which is okay because last index in text =", len(text)-1, "and a boxcar of", length
			if text[start_letter] in ignored_text:
				continue

			if self.DEBUG:
				print "-----------\nstart letter = ", text[start_letter]
			try:
				if self.DEBUG:
					print "expansion range is", range(0, len(text)-length-start_letter+1)
				for expansion in range(0, (len(text)-length-start_letter)+1):
					
					end_of_expansion = False
					
					end_letter = start_letter + length + expansion
					if self.DEBUG:
						print "end_letter = start_letter + length + expansion", end_letter, '=', \
						start_letter, '+', length, '+', expansion

					if end_letter > len(text):
						if self.DEBUG:
							print "end_letter is", end_letter, "and is greater than or equal to len(text)", len(text), "BREAK"
						end_of_expansion = True
						break
					
					text_slice = text[start_letter:end_letter]
					
					if self.DEBUG:
						print "indices text[", start_letter, end_letter, "] and text slice is", text_slice
					
					if end_letter > len(text):
						if self.DEBUG:
							print "end of expansion... end_letter > len(text) BREAK"
						end_of_expansion = True
						break
					if len(text_slice) == len(text):
						if self.DEBUG:
							print "Not enough space for repeats of a slice of length", \
							len(text_slice), "in", len(text), "BREAK"
						end_of_expansion = True
						break
					try:
						left_slice = text[:(start_letter+len(text_slice)-1)]
						right_slice = text[(start_letter+1):]
						if self.DEBUG:
							print "left is", left_slice, "right is", right_slice, \
							"and text_slice", text_slice, "is in one?", \
							text_slice in left_slice or text_slice in right_slice
						if text_slice in left_slice or text_slice in right_slice:
							text_slice_list = [text_slice]
							if self.DEBUG:
								print ">>>>  adding", text_slice_list
							self.combinations.update(text_slice_list)
							if self.DEBUG:
								print ">>>>  combinations are: ", self.combinations
			 		except IndexError:
			 			if self.DEBUG:
			 				print "INDEX ERROR"
			 			end_of_text = True
			 			break
			 		if end_of_expansion:
						if self.DEBUG:
							print "BREAK out of expansion"
						continue
			except IndexError:
				if self.DEBUG:
					print "INDEX ERROR"
				break
			if end_of_text:
				if self.DEBUG:
					print "INDEX ERROR, END OF TEXT!"
				break
		return self.combinations.most_common()

	def snippets(self):
		pass


# also, make distances between non-overlapping repeats



