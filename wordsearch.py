#================================================================
# Crossword Puzzle generator Started March 28, 2001
# Finalized March 1st 2003
# General Public license Open Source project
# Author: Edward March WebSite: www.poetworld.org/~emarch/
# Updates to this puzzle can be found on march.freeshell.org
# Note: This crossword.py file was run thru pindent.py to
# provide "# end" markers. Part of pythoon-tools-1.5.2.rpm
# This code was tested with python version 2.0 under linux
# but should run under 1.5.2 and up.
#================================================================
import sys, string, random, copy, glob

VERSION = "Version 1.2 / March 1, 2003"

True = 1
False = 0
EMPTY = '.'

#================================================================
# Return the minimum value of a or b
#================================================================
def min(a,b):
    if(a < b):
        return(a)    
    # end if
    return(b)
# end def min

#================================================================
# Return the maximum value of a or b
#================================================================
def max(a,b):
    if(a > b):
        return(a)    
    # end if
    return(b)
# end def max

#================================================================
# A Puz class is a one question and word pair along with the 
# a y,x and direction character ('A' or 'D'). Note y,x order
# is easier to sort by across then x,y
# 
# A PuzList of Puz items that make up all the crossword 
# puzzle questions
#================================================================
class Puz:
    def __init__(self,word,question):
        self._question = question
        self._word = string.upper(word)
        self._direction = ()
    # end def __init__
    
    def setDirection(self,ad):
        self._direction = ad
    # end def setDirection
    
    def getDirection(self):
        return self._direction
    # end def getDirection
    
    def getWord(self):
        return self._word
    # end def getWord
    
    def getQuestion(self):
        return self._question
    # end def getQuestion
# end class Puz

#================================================================
# A Cell class is one square of the crossword puzzle. Its has the
# Letter of the word that belong there. It alos knows its tag (y,x)
# coordinate on the grid, and it gets a number such as 3 across 
# or 5 down once all the cells are or inplace in the grid. Even 
# empty cells that have no words - the black of the puzzle are
# still valid Cell objects.
#
# Inside each grid[y][x] is a Cell object. Each cell holds a 
# character, (and later a number) coordinate and direction as (y,x,'A')
# or (y,x,'D'). Naming the cell coordinate in Y,X not X,Y makes 
# the sorting easier to sort by Across and then Down.  
#================================================================
class Cell:
    def __init__(self,c=EMPTY,d=()):
        self._c = c
        self._direction = d
        self._num = " "
    # end def __init__
    
    def getChar(self):
        return self._c
    # end def getChar
    
    def setNum(self,n):
        self._num = n    
    # end def setNum
    
    def getNum(self):
        return self._num
    # end def getNum
# end class Cell

#================================================================
# The Crossword class hold all other class that make the puzzle.
# PuzList is a list of Puz with the 0th elment having the longest
# word because it is layed down first.
#
# When used as a library
# a = Crossword()
# a.add("Monday","First day back to work")
# a.setTitle("Days")
# a.generate()
#================================================================
class Crossword:
    def __init__(self):
        self.PuzList = []
        self.title = ""
        self.wordlist = False
        self.cellHeight = .4
        self.cellWidth = .4
        self.hint = 0       
        self.density = 1        
    # end def __init__
    
    def setWordList(self,v):
        self.wordlist = v
    # end def setWordList
    
    def setCellHeight(self,h):
        self.cellHeight = h 
    # end def setCellHeight
    
    def setCellWidth(self,w):
        self.cellWidth = w  
    # end def setCellWidth
    
    def setHintPercentage(self,v):
        self.hint = v   
    # end def setHintPercentage
    
    def setDensity(self,v):
        self.density = v    
    # end def setDensity
    
    def setTitle(self,title):
        self.title = title
    # end def setTitle
    
    def add(self,word,question):
        lw = len(word)
        # keep the longest word at the beginning of the list index 0
        if( len(self.PuzList) > 0 and lw > len(self.PuzList[0].getWord()) ):
            self.PuzList.insert(0, Puz(word,question) )
        else:
            self.PuzList.append( Puz(word,question) )
        # end if
    # end def add
    
    def _getSortedWords(self):
        l = []  
        for i in self.PuzList:
            l.append( i.getWord() )         
        # end for
        l.sort()
        return l
    # end def _getSortedWords
    
    def PrintQuestions(self):
        print "\nACROSS"
        for a in self.AcrossList:
            n = a[0]
            i = a[1]
            print "%d.%s" % (n,self.PuzList[i].getQuestion())       
        # end for
        
        print "\nDOWN"
        for a in self.DownList:
            n = a[0]
            i = a[1]
            print "%d.%s" % (n,self.PuzList[i].getQuestion())       
        # end for
    # end def PrintQuestions
    
    
    def PrintAscii(self,hint=100):
        for y in xrange(self.boundary[self.MINY], self.boundary[self.MAXY]+1):
            s = ""
            for x in xrange(self.boundary[self.MINX], self.boundary[self.MAXX]+1):
                c = self.grid[y][x].getChar()
                cn = self.grid[y][x].getNum()
                if(c == EMPTY):
                    s = s + cn + "#" + " "
                elif(hint < random.randint(1,100)):
                    s = s + cn + "_" + " "
                else:
                    s = s + cn + c + " "
                # end if
            # end for
            print s
            print       
        # end for
    # end def Print
    
    
    #================================================================
    # This starts the main generator which puts the longest word
    # in the center of the grid and then uses the recursive trial and
    # error method and soving the rest of the word placement.
    #================================================================
    def generate(self, width, height):
        self.width = 1+width+1
        self.height = 1+height+1
        self.grid = [] # arrary of array of lists indexed by [y][x]
        #
        self.MINX = 0 # boundry offsets
        self.MAXX = 1
        self.MINY = 2
        self.MAXY = 3           
        self.boundary = [width,0,height,0]
        self.boundary[self.MINX] = self.width-1 
        self.boundary[self.MAXX] = 1    
        self.boundary[self.MINY] = self.height-1    
        self.boundary[self.MAXY] = 1
        #
        self.grid= []
        # a 10x10 puzzle has a guard border around it
        # so its really 12x12 and word fit from 1..10 x 1..10
        # leaving 0 and 11 always empty for below,above,right,left guards       
        for y in xrange(0,self.height+2):
            self.grid.append([])
            for x in xrange(0,self.width+2):        
                self.grid[y].append( Cell())
            # end for
        # end for
        
        # Put the longest word (at index zero) in center of the
        # puzzle grid as this gives us good possibilities of 
        # laying down other words rather easily. 
        P = self.PuzList[0]
        word = P.getWord()
        l = len(word)           
        x = min((self.width-1)/2 - (l/2), 1)
        y = self.height/2
        self._assignAcross(x,y,P)
        #
        # OK, go make a puzzle using the rest of the words!!
        #
        for attempt in range( len(self.PuzList)-1 ):
            ok = self._genRecursive(1)
            if(ok== True):
                self._sortQuestions()
                break
            # end if    
            
            print "Stuck! Shuffling word order for attempt #",attempt+2
            self.PuzList.append( self.PuzList[attempt+1] )
            del self.PuzList[attempt+1] 
        # end for 
        if(ok != True):
            print "Error: Giving up. Failed to generate puzzle. Perhaps the"
            print "across/down sizes are too small for the number"
            print "words. Try increasing the across and/or down."
            print "Or try reducing the number of words."
        # end if
    # end def generate
    
    #================================================================
    # Recursive generator. give word index - the heart of the issue
    # the crux of the problem of finding out what words will be where.
    #
    # This functions calls itself with the next word and keeps the grid 
    # on the stack. The grid is saved to SaveGrid and the next new word 
    # is placed.  This continues until all words are placed. But in 
    # reality we get stuck and can not place a word, so  we backtrack 
    # and restore have to restore the grid (which removes the last word 
    # placed) and try a new position for that word. 
    #================================================================
    def _genRecursive(self,i):  
        if(i >= len(self.PuzList) ):
            return True
        # end if
        
        word = self.PuzList[i].getWord()
        lw = len(word)
        wo = lw-1
        SaveGrid = copy.deepcopy(self.grid)
        SaveBoundary = self.boundary[:]
        
        #
        # Keep running border sizes, we only use the
        # cells available no matter how big we can really go.
        # 
        y1 = max(1,self.boundary[self.MINY]-wo)
        y2 = min(self.height-2,self.boundary[self.MAXY]+wo)
        x1 = max(1,self.boundary[self.MINX]-wo)
        x2 = min(self.width-2,self.boundary[self.MAXX]+wo)
        
        for d in xrange(self.density,0,-1):            
            for y in xrange(y1,y2):
                for x in xrange(x1,x2):
                    if(x+wo < self.width-2 and self._doesWordFitAcross(i,x,y,d) == True):
                        if(self._genRecursive(i+1) == True):
                            return True
                        # end if
                        self.grid = copy.deepcopy(SaveGrid)
                        self.boundary = SaveBoundary[:]
                    elif(y + wo < self.height-2 and self._doesWordFitDown(i,x,y,d) == True):
                        if(self._genRecursive(i+1) == True):
                            return True
                        # end if
                        self.grid = copy.deepcopy(SaveGrid)
                        self.boundary = SaveBoundary[:]
                    # end if
                # end for
            # end for
        # end for
        self.grid = copy.deepcopy(SaveGrid)             
        self.boundary = SaveBoundary[:]
        self.PuzList.append( self.PuzList[i] )
        del self.PuzList[i] 
        return False
    # end def _genRecursive
    
    
    #================================================================
    # Return True if word at index i fits at location x,y with a
    # density. Density determines how many letters are in common.
    # If the density was less than 1 there would be no CROSS in the
    # crossword puzzle. A desnity of two means this word has to
    # fit by using two letters from words already on the grid.
    # Higher desnitys are harder for the computer to generate by easier
    # for the human to solve as there is more hints of the letters.
    #================================================================
    def _doesWordFitAcross(self, i, x, y,density):
        word = self.PuzList[i].getWord()
        lw = len(word)
        xx = x+lw
        hits = 0
        consecutive = 0
        # Must be a empty space before nad after me 
        # we can not rn words together.
        cLeft = self.grid[y][x-1].getChar()
        cRight= self.grid[y][x+lw].getChar()
        if(cLeft != EMPTY or cRight != EMPTY):
            return False;       
        # end if
        
        # Make sure each letter has either an empty 
        # cell or the correct letter we need.
        for tx in xrange(x,xx):
            wc = word[tx-x]                 # word character
            c = self.grid[y][tx].getChar() # character on the puzzle
            if(c != EMPTY and c != word[tx-x]):
                return False # wrong letter in my spot.
            # end if
            
            # Now look one line above and below and make sure 
            # they're are all empty. We're not trying to invent words!
            cAbove = self.grid[y-1][tx].getChar()
            cBelow = self.grid[y+1][tx].getChar()
            if(c == EMPTY and (cAbove != EMPTY or cBelow != EMPTY) ):
                return False
            # end if
            
            # If we share a letter its a hit, bu watchout for
            # two consectutive hits else we have substrings of words
            # and thats not fair.
            if(c == wc):
                hits = hits + 1            
                consecutive = consecutive + 1          
                if(consecutive > 1):
                    return False # avoid substringing                    
                # end if
            else:
                consecutive = 0
            # end if
        # end for
        if(hits >= density):
            self._assignAcross(x,y,self.PuzList[i])
            return True                
        # end if
        return False
    # end def _doesWordFitAcross
    
    
    #================================================================
    # Return True if word at index i fits at location x,y with a
    # density. Density determines how many letters are in common.
    # If the density was less than 1 there would be no CROSS in the
    # crossword puzzle. A desnity of two means this word has to
    # fit by using two letters from words already on the grid.
    # Higher desnitys are harder for the computer to generate by easier
    # for the human to solve as there is more hints of the letters.
    #================================================================
    def _doesWordFitDown(self, i, x, y, density):
        word = self.PuzList[i].getWord()
        lw = len(word)
        yy = y+lw
        hits = 0
        consecutive = 0
        cAbove = self.grid[y-1][x].getChar()
        cBelow= self.grid[y+lw][x].getChar()
        if(cAbove != EMPTY or cBelow != EMPTY):
            return False;       
        # end if
        
        for ty in xrange(y,yy):
            wc = word[ty-y]
            c = self.grid[ty][x].getChar()
            if(c != EMPTY and c != wc):
                return False
            # end if
            cLeft = self.grid[ty][x-1].getChar()
            cRight = self.grid[ty][x+1].getChar()
            if(c == EMPTY and (cLeft != EMPTY or cRight != EMPTY) ):
                return False
            # end if
            if(c == wc):
                hits = hits + 1            
                consecutive = consecutive + 1        
                if(consecutive > 1):
                    return False                     
                # end if
            else:
                consecutive = 0
            # end if
        # end for
        if(hits >= density):
            self._assignDown(x,y,self.PuzList[i])
            return True                
        # end if
        return False
    # end def _doesWordFitDown
    
    
    #================================================================
    # Assign the Puz object at x,y to be set in the horizontal mode.
    #================================================================
    def _assignAcross(self,x,y,P):
        lw = len(P.getWord())
        tag=(y,x,'A')
        P.setDirection(tag)
        self.grid[y][x] = Cell(P.getWord()[0],tag)
        for xx in range(x+1,x+lw):
            self.grid[y][xx] = Cell(P.getWord()[xx-x])
        # end for
        self._bound(x,y)
        self._bound(x+lw-1,y)
    # end def _assignAcross
    
    #================================================================
    # Assign the Puz object at x,y to be set in the vertical mode.
    #================================================================
    def _assignDown(self,x,y,P):
        lw = len(P.getWord())
        tag = (y,x,'D')
        P.setDirection(tag)
        self.grid[y][x] = Cell(P.getWord()[0],tag)
        for yy in range(y+1,y+lw):
            self.grid[yy][x] = Cell(P.getWord()[yy-y])
        # end for
        self._bound(x,y)
        self._bound(x,y+lw-1)
    # end def _assignDown
    
    #================================================================
    # Kep widest/highest bounds on grid, we dont print 
    # what we dont use.
    #================================================================
    def _bound(self,x,y):
        if(x < self.boundary[self.MINX]):
            self.boundary[self.MINX] = x
        # end if
        if(x > self.boundary[self.MAXX]):
            self.boundary[self.MAXX] = x
        # end if
        if(y < self.boundary[self.MINY]):
            self.boundary[self.MINY] = y
        # end if
        if(y > self.boundary[self.MAXY]):
            self.boundary[self.MAXY] = y
        # end if
    # end def _bound
    
    
    #================================================================
    # This is what many other forget to do. Here we make the puzzle
    # look nice, until now all numbering was for the computers sake.
    # We now number the cells in a nice human order and relate them
    # to the questions. Like a good old fashioned puzzle should look.
    # Sort the questions based on the Y,X coordinates to the
    # cells can be numbered in order left to right and downwards.
    # Then the questions are indexed to match, so 1 Across
    # becomes the correct words for the cell numbered 1 with
    # a word inserted horizontally.
    #================================================================
    def _sortQuestions(self):
        self.AcrossList = [] # index to PuzList
        self.DownList = []   # index to PuzList
        #
        order = [] # a list of (y,x,c,i) wher c='A' or 'D' and i = PuzList index
        for i in xrange(len(self.PuzList)): 
            p = self.PuzList[i]
            order.append(p.getDirection()+(i,)) # add i into tuple          
        # end for
        order.sort() # sorted by y then x
        number = 1
        ox = 0
        oy = 0  
        for n in order:
            y = n[0]
            x = n[1]        
            ad = n[2]
            i = n[3]
            if(ad == 'A'):
                self.AcrossList.append((number,i))              
                self.grid[y][x].setNum("%d" % number)
            else:
                if(x == ox and y == oy):
                    number = number - 1     
                # end if
                self.DownList.append((number,i))                
                self.grid[y][x].setNum("%d" % number)
            # end if
            ox = x
            oy = y      
            number = number + 1
        # end for
    # end def _sortQuestions
    
    #================================================================
    # Make string suitable for postscript 'show'
    # by escaping parenthesis characters   
    #================================================================
    def _ps_show(self,s):
        s = string.strip(s)
        string.replace(s,'(','\\(')
        string.replace(s,')','\\)')
        string.replace(s,'\n','\\n')
        return s
    # end def _ps_show
    
    #================================================================
    # Generate a post script file for a nice printout
    # the command line tool ps2pdf can be used for a nicer smaller
    # PDF file.
    #================================================================
    def Postscript(self,fname,hint=100):
        if(hint == 0):
            hint = self.hint
        # end if
        
        ps = open(fname,"wt")
        ps.write("%!\n%% crossword puzzle\n")
        ps.write("% Convert inches->points (1/72 inch)\n")
        ps.write("/inch { 72 mul } def\n")
        ps.write("%%Page 1 2\n")
        ###
        ps.write("/square { newpath moveto gsave 0 setlinewidth\n")
        ps.write("%g inch 0 inch rlineto\n"  % (self.cellWidth))
        ps.write("0 inch %g inch  rlineto\n" % (-self.cellHeight))
        ps.write("%g inch 0 inch rlineto\n"  % (-self.cellWidth)) 
        ps.write("closepath\n")
        #white out a cell and frame it
        ps.write("gsave 0 setlinewidth 1 setgray fill grestore\n")
        ps.write("stroke grestore\n")
        ps.write("gsave .01 inch -.1 inch rmoveto /Courier-New-Bold findfont 7 scalefont setfont show grestore\n")
        ps.write(".1 inch %g inch rmoveto /Courier-New findfont 20 scalefont setfont show }def\n" % (-self.cellHeight+.1))
        ###
        l = len(self.title)
        x = (8.5 - (l * .2))/2
        y = 10.68   
        ps.write("%g inch %g inch moveto " % (x,y))
        ps.write("/Courier-New-Bold findfont 20 scalefont setfont (%s) show\n" % (self._ps_show(self.title)))
        width = self.cellWidth * (self.boundary[self.MAXX] - self.boundary[self.MINX] + 1)
        height= self.cellHeight * (self.boundary[self.MAXY] - self.boundary[self.MINY] + 1)
        puzX = (8.5 - (width))/2
        puzY = 10.6 
        ps.write("%Gray Area under puzzle\n")
        ps.write("gsave newpath %g inch %g inch moveto\n" % (puzX,puzY) )       
        ps.write("%g inch 0 inch rlineto\n" % (width) )     
        ps.write("0 inch %g inch rlineto\n" %(-height) )        
        ps.write("%g inch 0 inch rlineto\n" %(-width) )     
        ps.write("closepath 1 setlinewidth 0.95 setgray fill stroke grestore\n")        
        yinch = puzY
        for y in xrange(self.boundary[self.MINY], self.boundary[self.MAXY]+1):
            xinch = puzX
            for x in xrange(self.boundary[self.MINX], self.boundary[self.MAXX]+1):
                c = self.grid[y][x].getChar()
                cn = self.grid[y][x].getNum()
                if(c != EMPTY):
                    if(hint < random.randint(1,100) ):
                        c = ' '         
                    # end if
                    ps.write("(%s) (%s) %g inch %g inch square\n" %(c,cn,xinch,yinch) )
                # end if
                xinch = xinch + self.cellWidth
            # end for
            yinch = yinch - self.cellHeight
        # end for
        
        fontheight = .19
        qcount = max( len(self.AcrossList), len(self.DownList) ) 
        qheight = .5 + (fontheight * qcount)
        ps.write("/Times-Roman findfont 12 scalefont setfont\n")
        ps.write(".6 inch %g inch moveto (ACROSS) show\n" % qheight)
        yinch = qheight - .3
        for a in self.AcrossList:
            n = a[0]
            i = a[1]
            ps.write(".6 inch %g inch moveto (%d. %s) show\n" % (yinch,n,self.PuzList[i].getQuestion()) )    
            yinch = yinch - fontheight      
        # end for
        
        ps.write("4 inch %g inch moveto (DOWN) show\n" % qheight)
        yinch = qheight - .3
        for a in self.DownList:
            n = a[0]
            i = a[1]
            ps.write("4 inch %g inch moveto (%d. %s) show\n" % (yinch,n,self.PuzList[i].getQuestion())  )    
            yinch = yinch - fontheight
        # end for
        
        
        #
        # Show the [optional] word list to make the puzzle much easier.
        #               
        if(self.wordlist != False):
            ytop = (puzY - height) - .25
            ps.write("/Times-Roman findfont 9 scalefont setfont\n")
            ps.write("1.5 inch %g inch moveto (Words) show\n" % ytop)
            fontheight = .1         
            ytop = ytop -.2
            w = self._getSortedWords()
            xleft = .7
            x = xleft           
            y = ytop
            longestword = 0
            for a in w:
                ps.write("%g inch %g inch moveto (%s) show\n" % (x,y,a))    
                if(len(a) > longestword):
                    longestword = len(a) # track longest word in column                 
                # end if
                y = y - fontheight      
                if(y  < ytop - .6):
                    y = ytop
                    x = xleft + (.1 * longestword) + .3
                    xleft = x                                                       
                # end if
            # end for
        # end if
        
        ps.write("%%EndPage\n%%Page\nshowpage\n")
        ps.close()
    # end def Postscript
# end class Crossword


#================================================================
# Read input source files *.txt and make two 
# files *.ps and *.answer.ps files from each .txt file.
#================================================================
def main():
    if(len(sys.argv) < 2):
        print "Crowssword Puzzle Generator ",VERSION
        print "Author: Edward March (march.freeshell.org)"
        print "Usage: python Crossword.py  myfile1.txt | *.txt [myfile2.txt]"
        print "\n"
    # end if

    comments = '#/;.-*@'
    for i in range(1,len(sys.argv)):
        paramAcross = paramDown = 20
        wordcount = 0
        for fname in glob.glob(sys.argv[i]):
            f = open(fname)
            cwp = Crossword()
            for s in f.readlines():
                l = string.split(s,':')
                if(len(l) == 2 and not l[0][0] in comments):
                    cwp.add(string.strip(l[0]),string.strip(l[1]))
                    wordcount = wordcount + 1
                # end if
                l = string.split(s,'=')
                if(len(l) == 2 and not l[0][0] in comments):        
                    s = string.strip( string.lower(l[0]) )
                    v = l[1]        
                    if(s == "across"):
                        paramAcross = string.atoi(v)               
                    # end if
                    if(s == "down"):
                        paramDown = string.atoi(v)             
                    # end if
                    if(s == "title"):
                        cwp.setTitle(v)
                    # end if
                    if(s == "wordlist"):
                        cwp.setWordList(string.atoi(v))
                    # end if
                    if(s == "density"):
                        cwp.setDensity(string.atoi(v))
                    # end if
                    if(s == "hints"):
                        cwp.setHintPercentage(string.atoi(v))
                    # end if
                    if(s == "cellheight"):
                        cwp.setCellHeight(string.atof(v))
                    # end if
                    if(s == "cellwidth"):
                        cwp.setCellWidth(string.atof(v))
                    # end if
                # end if
            # end for
            f.close()
            print "Generating %d word puzzle, %d across by %d down." % (wordcount,paramAcross,paramDown)
            cwp.generate(paramAcross,paramDown)
            cwp.PrintAscii(100)
            
            fnameps = string.replace(fname,".txt","")
            fname1 = fnameps + ".ps"
            fname2 = fnameps + ".answer.ps"
            cwp.Postscript(fname1,0)
            cwp.Postscript(fname2,100)
            print "Done. Files written: %s and %s" % (fname1,fname2)
        # end for
    # end for
# end def main

#================================================================
# If started from the command line invoke the main fnction and 
# run as a stand alone tool. Otherwise we are  probably being 
# used as a Crossword class library.
#================================================================
if __name__ == "__main__":
    main()
# end if        
