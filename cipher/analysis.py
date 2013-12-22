import sys
from collections import Counter
from math import trunc
import ignore_characters

"""
This module uses a boxcar method to find common (>1 instance) patterns in a text.
Needs the ignore_characters.py configuration file, with lists "automatic" and "user_added"
to add or subtract characters from the analysis (' ', '\ n' and '\ t' ignored by default).

Frequency class: specify filename if run as a stand-alone, or pass text to class instance on import.
"""


class Frequency(object):

	def __init__(self, text, length=3):
		self.text = text
		self.length = length
		
	def boxcar(self, length=3):
		DEBUG = True
		ignored_text = ignore_characters.automatic + ignore_characters.user_added
			
		self.combinations = Counter()

		end_of_text = False
		if DEBUG:
			print "length of text:", len(text)
			print "length of boxcar", length

		last_boxcar = len(text) - length + 1
		if DEBUG:
			print "last_boxcar =", last_boxcar

		for start_letter in range(0, last_boxcar):		
			if DEBUG:
				print "\n-----------\ntext[",start_letter, "] range", range(0, last_boxcar), "which is okay because last index in text =", len(text)-1, "and a boxcar of", length
			if text[start_letter] in ignored_text:
				continue

			if DEBUG:
				print "-----------\nstart letter = ", text[start_letter]
			try:
				if DEBUG:
					print "expansion range is", range(0, len(text)-length-start_letter+1)
				for expansion in range(0, (len(text)-length-start_letter)+1):
					
					end_of_expansion = False
					
					end_letter = start_letter + length + expansion
					if DEBUG:
						print "end_letter = start_letter + length + expansion", end_letter, '=', start_letter, '+', length, '+', expansion

					if end_letter > len(text):
						if DEBUG:
							print "end_letter is", end_letter, "and is greater than or equal to len(text)", len(text), "BREAK"
						end_of_expansion = True
						break
					
					text_slice = text[start_letter:end_letter]
					
					if DEBUG:
						print "indices text[", start_letter, end_letter, "] and text slice is", text_slice
					
					if end_letter > len(text):
						if DEBUG:
							print "end of expansion... end_letter > len(text) BREAK"
						end_of_expansion = True
						break
					if len(text_slice) == len(text):
						if DEBUG:
							print "Not enough space for repeats of a slice of length", len(text_slice), "in", len(text), "BREAK"
						end_of_expansion = True
						break
					try:
						left_slice = text[:(start_letter+len(text_slice)-1)]
						right_slice = text[(start_letter+1):]
						if DEBUG:
							print "left is", left_slice, "right is", right_slice, "and text_slice", text_slice, "is in one?", text_slice in left_slice or text_slice in right_slice
						if text_slice in left_slice or text_slice in right_slice:
							text_slice_list = [text_slice]
							print ">>>>  adding", text_slice_list
							self.combinations.update(text_slice_list)

							print ">>>>  combinations are: ", self.combinations
			 		except IndexError:
			 			if DEBUG:
			 				print "INDEX ERROR"
			 			end_of_text = True
			 			break
			 		if end_of_expansion:
						if DEBUG:
							print "BREAK out of expansion"
						continue
			except IndexError:
				if DEBUG:
					print "INDEX ERROR"
				break
			if end_of_text:
				if DEBUG:
					print "SOMEONE THREW AN END OF TEXT!"
				break
		return self.combinations.most_common()

	def snippets(self):
		pass



# have overlapping patterns for this analysis.
# make analysis for non-overlapping patterns.
# also, make distances between repeats


		

if __name__ == "__main__":

	# filename = sys.argv[1]

	# with open(filename, 'r') as f:
	#  	text = f.read()
	#  	a_count = Frequency(text)
	#  	boxcar_freqencies = a_count.boxcar()
	#  	print boxcar_freqencies

	text = "abcabcabc"
	a_count = Frequency(text)
 	boxcar_freqencies = a_count.boxcar()
	print boxcar_freqencies

