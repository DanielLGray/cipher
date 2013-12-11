import sys
from random import shuffle
from os.path import basename
''' Takes plaintext argument and encrypts/decrypts according to a random key. ''' 

# have alphabet as set or as list?



class plaintext(object):
	''' Has filename and text attributes '''

	def __init__(self, filename):
		self.filename = filename
		with open(filename, 'r') as f:
			self.text = f.read()

class key(object):
	''' Has dictionary attribute. Unless a key dictionary is specfied in the arguments, 
	will randomly generate one. ''' 

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
		if dictFilename:
			with open(dictFilename, 'r') as f:
				self.dictionary = f.read()
		return self.dictionary

	def generate_key(self):

		
		# make a copy of the shuffled list
		cipherLETTERS = list(self.ALPHABET)
		# use random.shuffle
		shuffle(cipherLETTERS)
		self.dictionary = dict(zip(self.ALPHABET, cipherLETTERS))
		return self.dictionary

class cipher(object):
	
	def __init__(self):
		self.plaintext = plaintext
		self.key = key
		self.cipherTEXT = ''
		self.problemLetters = []

	def ciphertext(self, plaintext, key):
		plainTEXT = plaintext.text.upper()		
		# write as generator next
		for LETTER in plainTEXT:
			try: 
				cipherLETTER = key.dictionary[LETTER]
			# figure out what type that these errors are
			except Exception, e:
				cipherLETTER = LETTER
				self.problemLetters.append(LETTER)
			self.cipherTEXT += cipherLETTER
		return self.cipherTEXT, self.problemLetters

	def encipher(self, plaintext, key):
		self.ciphertext(self, plaintext, key)
# write with option to remove whitespace

	# with open('cipherTEXT of %s' %basename(plaintext.filname), 'a') as f:
	# 	f.write(cipherTEXT)

	# with open('generated_key' % plainTEXT.filename, 'a') as f:
	# 		# Can only print strings, so change dictionary to string.
	# 	f.write(str(self.dictionary))
		

		
	def decipher():
		pass


#! scripts
if __name__ == '__main__':

	someText = plaintext(sys.argv[1])
	
	someKey = key()
	
	# try:
	# 	someKey.read_key(sys.argv[2])
	# except Exception, e:
	# 	someKey.generate_key()

	someCipher = cipher()
	a_key = someKey.generate_key()
	print a_key
	print someCipher.ciphertext(someText, someKey)

			
