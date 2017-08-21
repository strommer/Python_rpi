import sys
import random

def scramble_word(word):
	if (len(word) < 4):
		return word
	else:
		temp = [c for c in word[1:-1]]
		random.shuffle(temp)
		x = "".join(temp)
		return word[0] + x + word[-1]

def scramble_text(text):
	words = text.split()
	list_word = [scramble_word(word) for word in words]
	return " ".join(list_word)

def scramble_file(filename):
	f = open(filename).readlines()
	list_text = [scramble_text(text).split("\n") for text in f]
	for x in list_text:
		print (" ".join(x))

if __name__ == "__main__":
        if len(sys.argv) == 1:
          print("No arguments passed.  We'll prompt user for text.")
        else:
          print("Files to be processed: " + str(sys.argv[1]))
          #f = open(sys.argv[1]).readline()
          print(scramble_file(sys.argv[1]))
else:
        print("Imported.  User is planning to invoke functions directly")