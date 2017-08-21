import argparse
import sys
import os



parser = argparse.ArgumentParser(description='emulation of linux wc')

parser.add_argument('-c', '--bytes', action="store_true", default=False,
                    help ="prints the number of bytes")
parser.add_argument('-w', '--words', action="store_true", default=False,
                    help = "print the word counts")
parser.add_argument('-l', '--lines', action="store_true", default=False,
                    help = "print the lines count")
parser.add_argument('-m', '--chars', action="store_true", default=False,
                    help = "print the character count")
parser.add_argument('-L', '--max-line-length', action="store_true", default=False,
                    help = "print the length of longest line")


parser.add_argument("FILE", type=str, nargs="*" )

args = parser.parse_args()

if args.FILE :
    sum_no_of_bytes = sum_no_of_words = sum_no_of_lines = 0
    sum_no_of_chars = sum_no_of_longestline = 0
    
    if (args.bytes == False and args.words == False
        and args.lines == False and args.chars == False
        and args.max_line_length == False):
        args.bytes = args.words = args.lines = True

    
    for fin in args.FILE:
        if args.bytes == True:
            b = os.path.getsize(fin)
            print(b, end="  ")
            sum_no_of_bytes +=b

        if args.words == True:
            with open(fin) as f:
                x = len(f.read().split())
                print(x, end="  ")
                sum_no_of_words += x
                
        if args.lines == True:
            with open(fin) as f:
                y = sum(1 for line in f)
                print(y, end = "    ")
                sum_no_of_lines += y

        if args.chars == True:
            with open(fin) as f:
                num_chars = 0
                for line in f:
                    num_chars += len(line)
                print(num_chars, end = "    ")
                sum_no_of_chars +=num_chars

        if args.max_line_length == True:
            longestline =""
            with open(fin) as f:
                for line in f:
                    if len(line) > len(longestline):
                        longestline = line
                print(len(longestline), end ="  ")
                sum_no_of_longestline +=len(longestline)
                
        print(fin)

    if len(args.FILE) > 1:
        if args.bytes == True:
            print(sum_no_of_bytes, end = "  ")
        if args.words == True:
            print(sum_no_of_words, end = "  ")
        if args.lines == True:
            print(sum_no_of_lines, end = "  ")
        if args.chars == True:
            print(sum_no_of_chars, end = "  ")
        if args.max_line_length == True:
            print(sum_no_of_longestline, end ="    ")

else:
    var = input("Enter something")

        


    

    
