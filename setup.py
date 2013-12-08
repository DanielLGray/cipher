try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'Cryptography tools for ciphers',
	'author' : 'Daniel Gray',
	'url' : 'https://github.com/DanielLGray',
	'download url' : 'https://github.com/DanielLGray/cipher/',
	'author_email' : 'dgray60@gmail.com',
	'version' : '0.1',
	'install_requires' : 'nose',
	'packages' : ['cipher'],
	'scripts' : [],
	'name' : 'cipher',
}

setup(**config)
