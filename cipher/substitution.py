import sys
import random

''' Takes text argument and encrypts/decrypts according to a random key. ''' 

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
		
	def read_key(self, dictFilename):
		if dictFilename:
			with open(dictFilename, 'r') as f:
				self.dictionary = f.read()
		return self.dictionary

	def generate_key(self):

		ALPHABET = [
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

		cipherLETTERS = random.shuffle(ALPHABET)
		self.dictionary = dict(zip(ALPHABET, cipherLETTERS))
		
		with open('randomkey.txt', 'a') as f:
			r.write(key.dictionary)


		return self.dictionary



class cipher(object):
	
	def __init__(self, text, key):
		pass


	def encipher():
		pass		
		
		
	def decipher():
		pass


#! scripts
if __name__ == '__main__':

	someText = plaintext(sys.argv[1])
	 
	someKey = key()
	
	try:
		someKey.read_key(sys.argv[2])
	except Exception, e:
		someKey.generate_key()

	print someKey.dictionary