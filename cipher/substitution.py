import sys
import random

''' Takes text argument and encrypts/decrypts according to a random key. ''' 

# have alphabet as set or as list?
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




class plaintext(object):
	''' Has filename and text attributes '''

	def __init__(self, filename):
		self.filename = filename
		with open(filename, 'r') as f:
			self.text = f.read()


class key(object):
	''' Has dictionary attribute. Unless a key dictionary is specfied in the arguments, 
	will randomly generate one. ''' 

	def __init__(self, dictFilename):
		self.dictFilename = dictFilename
		try:
			with open(dictFilename, 'r') as f:
				self.dictionary = f.read()
		except Exception, e:
			self.dictionary = dictionary

	def generate():
		pass

def key_generator():
	


class cipher(object):
	
	def __init__(self, text, key):


		with open(key.name, 'r') as f:
			r.write(key.dictionary)


	def encipher():
		
		
		
	def decipher():
		pass


#! scripts
if __name__ == '__main__':

	someText = plaintext(sys.argv[1])
	# print someText.text
	
	someKey = key(sys.argv[2])
	print someKey.dictionary