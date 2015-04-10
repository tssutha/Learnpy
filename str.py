
import string
#palindrome  texts

def palindrome_1(s):
	print "palindrome_1 :  %s", s
	if s[0] != s[-1]:
		return False
	elif not s[1:-1]:
		return True
	else:
		return palindrome_1(s[1:-1])
		
def palindrome_2(s):
	print "palindrome_2 : %s", s
	return s == s[::-1]
	
def palindrome_3(s):
	s = str(s)
	print "palindrome_3 : %s", s
	return s == reversed(s)	
		
#print palindrome_1("teet")
#print palindrome_2("teet")
#print palindrome_3("teet")

#draw grid

#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +

def drawplus():
	print "+ ",

def drawdash():
	print "- ",

def drawbar():
	print "| ",

def drawspace():
	print "  ",
	
	
def drawrow(nCol, f1, f2, colsize):
	f1()
	for j in range(nCol):
		for i in range(colsize):
			f2()
		f1()
	print  

	
def drawgrid(row,col, rowsize, colsize):
	"""
	Draw a Grid based on given condition,
		row - number of rows
		col - number of cols
		rowsize - width of col 
		colsize - height of row
	"""
	drawrow(col,drawplus, drawdash, colsize)
	for	i in range(row):
		for i in range(rowsize):
			drawrow(col,drawbar, drawspace, colsize)
		drawrow(col,drawplus,drawdash, colsize)
		
	
#drawrow(2,drawplus, drawdash)

	
	
			
#drawgrid(5,5,1,1)

#print "*********************************************"

#drawgrid(5,5,2,2)

#print "********************************************"

#drawgrid(5,5,2,3)



#right justify

maxlen = 20;
def definesize():
	for i in range(maxlen):
		print "*",
	print

def right_justify(s, c):
	x = len(str(s))
	print "%d" % x
	for i in range(maxlen-x):
		print c,
	print s
	
def justifyword(s, con, wordsize):
	"""
		Justify a given word by give length based on conditon
		l - leftjustify r - rightjustify c - centered 
		other - centered with * wildcard
	"""
	if con.lower() == 'l':
		s = "{0:<{1}}".format(s, wordsize)
	elif con.lower() == 'r':
		s = "{0:>{1}}".format(s, wordsize)
	elif con.lower() == 'c':
		s = "{0:^{1}}".format(s, wordsize)
	else:
		s = "{0:*^{1}}".format(s, wordsize)
	return s	
	
#print justifyword("Sutha",'L',50)
#print justifyword("Sutha",'C',50)
#print justifyword("Sutha",'r',50)
#print justifyword("Sutha",'a',50)

#definesize()
#right_justify("sutha", '$')

##################################################
def isPowerOf(a,b):
	if a == b:
		return True
	elif a % b == 0:
		return isPowerOf(a/b, b)
	else:
		return False
		
#print "(%d,%d) = %r" % (9, 3,isPowerOf(9,3))
#print "(%d,%d) = %r" % (800, 20,isPowerOf(800,20))
#print "(%d,%d) = %r" % (100, 9,isPowerOf(100,9))
#print "(%d,%d) = %r" % (49, 7,isPowerOf(49,7))
#print "(%d,%d) = %r" % (27, 3,isPowerOf(27,3))
#print "(%d,%d) = %r" % (64, 2,isPowerOf(64,2))

######
	
class Point(object):
	def __init__(self,x,y):
		self.x, self.y = x, y
	def __str__(self):
		return 'Point({self.x}, {self.y})'.format(self = self)

#print str(Point(3,4))
#print str(Point(2, -10))	

#Nested Formatter Test
def nestedFormatter(width):
	for i in range(1,10):
		for base in 'dXob':
			print '{0:{width}{base}}'.format(i,width=width, base=base),
		print

#nestedFormatter(10)

# ROT N Encryption / Decryption 
def rot13(s, n, b):
	sl = list(s)
	startUp = ord('A')
	startLo = ord('a')
	if b == True: #encrypt ROT_n
		for i in range(len(s)):
			if(sl[i].isupper()):
				sl[i] =  chr(((ord(sl[i]) - startUp) + n)%26 + startUp)
			else:
				sl[i] =  chr(((ord(sl[i]) - startLo) + n)%26 + startLo)
	else: #decrypt ROT_N
		for i in range(len(sl)):
			if(sl[i].isupper()):
				sl[i] = chr(((ord(sl[i])-startUp) -n)%26 + startUp)
			else:
				sl[i] = chr(((ord(sl[i])-startLo) -n)%26 + startLo)
		
	return ''.join(sl)

	
#print "Sutha --> ROT13 -->%r" % rot13("MotherFucking",13, True)
#print rot13(rot13('MotherFucking',13,True),13,False)
	

#Think Python Chapter 9 : Case Study
#make use of word.txt file and do some work on string

def readall():
	f = open("words.txt",'r')
	count = 0;
	for line in f:
		count += 1
	print "Total Word : %d" % count
	f.close()
		

def readsomewithlength(n):
	f= open("words.txt", 'r')
	count =0
	for line in f:
		#print line,
		#print len(line.strip())
		if len(line.strip())>n:
			print line
			count += 1
	print count;
	f.close()
	

#readall()
#readsomewithlength(20)

	
def has_no_e(word):
	"""
	Checks whether the word contains letter e, if yes
	returns True otherwise False
	
	"""
	word.lower()
	if(word.find('e') >= 0):
		return False;
	else:
		return True
		
def has_no_e_1(word):
	"""
	Checks whether the word contains letter e, if yes
	returns True otherwise False
	
	"""
	for c in word:
		if 'e' in word:
			return False
		else:
			return True;
			
#print has_no_e_1("Sutha")
#print has_no_e("Sutha")

		
def analyzewords(filename, func):
	"""
		Analyse the content of given file using condition applied
		by func.
	"""
	fp = open(filename, 'r+')
	totalwords = 0
	specificwords = 0
	
	for line in fp:
		totalwords += 1
		if not func(line.strip()):
			specificwords += 1
			print line
	print totalwords
	print specificwords
	#print (((float(specificwords)/float(totalwords))*100.0)
	#return (float(totalwords), 
	#       float(specificwords),
	#       ((float(specificwords) / float(totalwords))*100.0))
	return (totalwords, specificwords)
	
#t = analyzewords("words.txt", has_no_e)
#s = "TotalWords : {0}, SpecificWords : {1} Percentage :{2:.2F}"
         #.format(t[0],t[1], float(float(t[1])/float(t[0]))*100.0  )
#s.format(t[0], t[1])
#print s
	
#avoid some letters

def avoid(s, fbc):
	"""
	Checks whether the string s contains any characters from fbc
	forbidden characters' if not return True otherwise False
	"""
	for c in list(fbc):
		#print s.find(c)
		if s.find(c) >= 0:
			return False
	return True


def avoid_1(s, fbc):
	"""
	Checks whether the string s contains any characters from fbc
	forbidden characters' if not return True otherwise False
	"""
	for c in fbc:
		if c in s:
			return False
	return True
	
print avoid('sutha', 'x')
print avoid_1('sutha','xb')
	
def analysewords1(filename, func, fbc):
	fin = open(filename,'r')
	count = 0
	for line in fin:
		if func(line.strip(),fbc):
			count += 1
	return count

#analyse word.txt file forbidden characters
#print "%d number of words doesn't contains this characters %r"
        # % (analysewords1("words.txt", avoid, "abc"), list("abc"))

		
def use_only(s, useonly):
	"""
		checks whether the given word is constructed using given use 
		only characters 
	"""
	useonly = useonly.lower()
	for c in list(s):
		c = c.lower()
		if useonly.find(c) < 0:
			return False
	return True

#print use_only("SuthAKBaran", "suthAakrn")

def use_all(s, useall):
	"""
		checks whether the given word s is using all the characters from
		useall list, consider lowercase and uppercase letters are treated
		as same
	"""
	s = s.lower()
	useall = useall.lower()
	for c in useall:
		if s.find(c) < 0:
			return False
	return True
	
#print use_all("Suthakaran", 'suthakrnm')
#print "%d number of words contain all vowels [%r]" % (analysewords1("words.txt",
		# use_all, "aeiou"), list("aeiou"))
#print "%d number of words contain all vowels [%r]" % (analysewords1("words.txt", 
        #use_all, "aeiouy"), list("aeiouy"))	

def is_abecedarian(word):
	"""
		check whether the characters in the string appears in alphabetical
		order
	"""		
	prevChar = 0;
	for c in word:
		#print "PrevChar : %d  ord  : %d" % (prevChar, ord(c.lower()))
		if prevChar <= ord(c.lower()):
			prevChar = ord(c.lower())
		else:
			return False
	return True
	
#print " is %s an abecedrian? %r" % ("egg",is_abecedarian("egg"))
			

def analysewords3(filename, func):
	fin = open(filename, 'r')
	count = 0
	for line in fin:
		if func(line.strip()):
			print line.strip().lower()
			count += 1
	return count
	
#print "Words.txt file contains %d numbers of abecedrian words" % 
     #analysewords3('words.txt', is_abecedarian)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	