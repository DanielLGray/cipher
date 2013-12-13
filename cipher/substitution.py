import sys, re
from random import shuffle
from os.path import basename
from itertools import groupby
''' Takes plaintext arguments and encrypts/decrypts according to a random key. ''' 


class plaintext(object):
	''' Has filename and text attributes '''

	def __init__(self, filename):
		self.filename = filename
		with open(filename, 'r') as f:
			self.text = f.read()

class key(object):
	''' Has dictionary attribute. Key can be instantiated using a file containing a key dictionary, 
	or the class can randomly generate one with the 'generate_key' method. ''' 

	def __init__(self, dictFilename=None):
		self.dictFilename = dictFilename
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

	def read_key(self, dictFilename):
		"""
		Reads a key from file. Requires a filename argument.
		"""
		if dictFilename:
			with open(dictFilename, 'r') as f:
				self.dictionary = f.read()
			return self.dictionary
		else:
			return IOError("Specify a Filename")

	def generate_key(self):
		"""
		Make a copy of the uppercase alphabet, shuffle the copy, and zip it with the original alphabet.
		"""
		cipherLETTERS = list(self.ALPHABET)
		shuffle(cipherLETTERS)
		self.dictionary = dict(zip(self.ALPHABET, cipherLETTERS))
		return self.dictionary

class cipher(object):
	"""
	Has plaintext, key, ciphertext, and problemLetters attributes. The first_pass method returns a 
	ciphertext with the problem letters it was unable to encipher, and the second_pass method calls 
	attempts to deal with them by expanding the key dictionary.
	"""
	def __init__(self):
		self.plaintext = plaintext
		self.key = key
		self.cipherTEXT = ''
		self.problemLetters = []

	def firstpass(self, plaintext, key):
		plainTEXT = plaintext.text.upper()		
		# rewrite as generator next
		for LETTER in plainTEXT:
			try: 
				cipherLETTER = key.dictionary[LETTER]
			# figure out what type that these errors are
			except Exception, e:
				cipherLETTER = LETTER
				self.problemLetters.append(LETTER)
			self.cipherTEXT += cipherLETTER
		return self.cipherTEXT, self.problemLetters

	def secondpass(self, cipherTEXT, problemLetters):
		"""
		Erases whitespaces.
		"""
		
		letters = [x[0] for x in list(groupby(problemLetters))]
		spaces = ['\t','\n', ' ']
		#erase whitespace
		for x in (set(letters) & set(spaces)):
			self. cipherTEXT = re.sub(x, '', self.cipherTEXT)

		return self.cipherTEXT 
	
	def encipher(self, plaintext, key):
		 
		ciphertext, problems = self.firstpass(plaintext, key)
		second = self.secondpass(ciphertext, problems)
		return second

	def output(self):
		pass
	# with open('cipherTEXT of %s' %basename(plaintext.filname), 'a') as f:
	# 	f.write(cipherTEXT)

	# with open('generated_key' % plainTEXT.filename, 'a') as f:
	# 		# Can only print strings, so change dictionary to string.
	# 	f.write(str(self.dictionary))
	


	def decipher():
		pass


#! scripts
if __name__ == '__main__':

	someText = plaintext('nathan.txt')
	someKey = key()
	
	# try:
	# 	someKey.read_key(sys.argv[2])
	# except Exception, e:
	# 	someKey.generate_key()
	someCipher = cipher()
	a_key = someKey.generate_key()
	# print a_key
	# print someCipher.firstpass(someText, someKey)
	# print someCipher.secondpass()
	print someCipher.encipher(someText, someKey)
			
