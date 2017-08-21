
import argparse
import sys


def word_count(s): 
	"""Returns the number of words in s. 
 
	The function s.split() is used to 
	convert s into a sequence of words; 
	the length of the sequence is returned. 
	
	>>> word_count("this and that") 
	3
	>>> word_count (b"The quick fox jumped over-the-lazy dog.")
	7
	""" 

	return len(s.split()) 


def line_count(s): 
	return len(s.splitlines()) 

def getparser():
	parser = argparse.ArgumentParser()
	parser.description = "Print newline, word, ..."
	parser.add_argument("filename", type=str, 
	help="Name of file", nargs="+") 
	parser.add_argument("-l", "--lines", 
	help="print the newline counts", 
	action="store_true") 
	parser.add_argument("-w", "--words", 
	help="print the word counts", 
	action="store_true") 

if __name__ == "__main__": 
	import doctest
	doctest.testmod()	
	args = getparser().parser.parse_args()
	for fn in args.filename: 
		data = open(fn,"rb").read() 
		if (args.lines):
			print(line_count(data)) 
		if (args.words): 
			print(word_count(data)) 
		if (args.bytes): 
			print(len(data)) 
		if (args.max_line_length): 
			print(max_line_length(data), end=" ") 
			print(fn) 
