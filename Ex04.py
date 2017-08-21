import sys
import random
import pprint

def swap_word(word):
	if (len(word) < 4):
		return word
	else:
		temp = [c for c in word[1:-1]]
		random.shuffle(temp)
		x = "".join(temp)
		return word[0] + x + word[-1]

def swap_text(text):
	words = text.split()
	list_word = [replace_word(word) for word in words]
	return " ".join(list_word)

def swap_file(filename):
	f = open(filename).readlines()
	list_text = [swap_text(text).split("\n") for text in f]
	for x in list_text:
		print (" ".join(x))

def make_dict(file1):
	f = open(file1)
	words = list(f)
	for i in range(len(words)):
		words[i] = words[i].rstrip()
	global word_dict 
	word_dict = dict()
	for word in words:
		if ((word[0],word[-1],len(word)) not in word_dict.keys()):
			word_dict[word[0],word[-1],len(word)] = [word]
		else:
			word_dict[word[0],word[-1],len(word)].append(word)

def replace_word(word):
	if (len(word) < 4):
		return word
	else:
		try:
			return random.choice(word_dict[word[1],word[-1],len(word)])
		except KeyError:
			return word

if __name__ == "__main__":
        if len(sys.argv) == 1:
          print("No arguments passed.  We'll prompt user for text.")
        else:
          print("This is the Dictionary: " + str(sys.argv[1]))
          print("This is the File to be changed: " + str(sys.argv[2]))
          #f = open(sys.argv[1]).readline()
          make_dict(sys.argv[1])
          print(swap_file(sys.argv[2]))
else:
        print("Imported.  User is planning to invoke functions directly")