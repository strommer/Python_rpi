import string
import sys

outfile = open('ospd.txt')

def func(wordlist,maxlen):
   if len(wordlist)==maxlen:
      printlist(wordlist)
   else:
      temp=''
      for i in range(0,len(wordlist)):
         temp = temp + wordlist[i][len(wordlist)]
      if temp in fixes:
         for word in fixes[temp]:
            func(wordlist+[word],maxlen)

def printlist(alist):
   for word in alist:
      outfile.write(word+"\n")
   outfile.write("*"*n+"\n")

print('Opening the file, reading words.')
wordfile = open(sys.argv[1],'r')
words = []
fixes = {}
n = int(sys.argv[2])

for word in wordfile:
   if(len(word.rstrip())==n):
      words.append(word.rstrip())

for i in range(0,n):
   for word in words:
      fixes.setdefault(word[0:i],[]).append(word)

for word in words:
   func([word],n)
   print word