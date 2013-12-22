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

	def __init__(self, text, minimum_boxcar_length=3):
		self.text = text
		self.minimum_boxcar_length = minimum_boxcar_length
		
	def boxcar(self, minimum_boxcar_length=3):
		ignored_text = ignore_characters.automatic + ignore_characters.user_added

		plaintext = list(text)
		complete_text = ''.join(plaintext)
				
		
		self.combinations = Counter()

		for n in range(0, len(plaintext)):		

			try:

				# if the character isn't one that should be considered, this will
				# skip this cycle of the iteration.
				for x in range(0, minimum_boxcar_length):
					if plaintext[n+x] in ignored_text:
						continue			

				# makes the boxcar a minimum of two characters
				# if ValueError (because the second character is beyond the end of list)
				# will skip this cycle of the iteration.

				boxcar_start_fragments = [plaintext[n]]
				for x in range(1, minimum_boxcar_length):
					boxcar_start_fragments.append(plaintext[n+x])

				boxcar = [reduce(lambda x, y: x + y, boxcar_start_fragments)]
				assert len(boxcar) == 1
				print boxcar
				if boxcar[0] in complete_text[:n] or boxcar[0] in complete_text[(n):]:
					self.combinations.update(boxcar)
					print "added!"
				else:
					print "not added!"
					continue



				# Finds plaintext[n+2] and adds to boxcar, until boxcar is equal 
				# in length to half of the list, since a repeat can only be as long as 
				# one half of the list, 
				for i in range(3, len(plaintext)-1):
					not_in_text = False
					try:

			 			if plaintext[n+i] in ignored_text:
							not_in_text = True 
							break

			 			boxcar = [reduce(lambda x, y: x + y, [boxcar[-1], plaintext[n+i]])]
						

			 			print boxcar[0], "inbefore", complete_text[:(n-1)], "inafter", complete_text[(n+1):]
						if boxcar[0] in complete_text[:(n)] or boxcar[0] in complete_text[(n+1):]:
							self.combinations.update(boxcar)
							print "added ", boxcar
						else:
							not_in_text = True
							break			
			 		
			 		except IndexError:
			 			break
					if not_in_text:
						break			

			except IndexError:
				continue

			
		return self.combinations.most_common()

	def snippets(self):
		pass



# have overlapping patterns for this analysis.
# make analysis for non-overlapping patterns.



		

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

