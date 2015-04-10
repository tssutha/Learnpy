import random
import time
from bisect import bisect_left


#sum of nested list

def sumof_nestedlist(ls, nls):
	"""
		Get the sum of nested list contains integer
	"""
	for li in ls:
		if isinstance(li, (list)):
			sumof_nestedlist(li, nls)
		else:
			nls.append(li)
		
	#print "Final %r" % nls
	return sum(nls)
	
numlist = [1,4,6,[10,11,13], [23,45],100,102]
nls = []

#print "sum of itmes in the list : %d" % sumof_nestedlist(numlist, nls )



def capitalize_all(t):
	"""
		capitalize the give word
	"""
	res = []
	for li in t:
		res.append(li.capitalize())
	return res
	
#print capitalize_all(['abbbd', 'A', 'SuthA'])


def capitalize_nested(t):
	"""
		Capitalize the given nested list
	"""
	res = []
	for li in t:
		if isinstance(li, (list)):
			res.append(capitalize_all(li))
		else:
			res.append(li.capitalize())
	return res
			

strlst = ["sutha", "a", "Amma", ["chev", "aruntha", "nick"], ["test", "bonDer"], "Damn"]

#print "BF %r" % strlst
#strlst = capitalize_nested(strlst)
#print "AF %r" % strlst




def middle(ls):
	return ls[1:-1]
	
ls = [1,2,3,5,6,7,8,9]
ls = middle(ls)
#print ls

def is_sorted(ls):
	"""
		check whether the list is sorted or not
		if yes
			return True
		else
			return False
	"""
	for i in range(len(ls)-1):
		if ls[i] > ls[i+1]:
			return False
		return True
		
ls = [1,2,4,5]
#print is_sorted(ls)

ls = ["Sutha", "abc"]
#print is_sorted(ls)

#print is_sorted(['b', 'a'])

def is_anagram(s1,s2):
	"""
		check whether the two words anagram
		Two words are anagram if you can rearrange the letters from
		one to spell the other
	"""
	if(len(s1) != len(s2)):
		return False
	
	for c in s1:
		count1 = s1.count(c)
		count2 = s2.count(c)
		if(count1 != count2):
			return False
		
		
	return True
			
			
#print "Is Anagram %r" % is_anagram("SUthab", "aUShtc")
#print "Is Anagram %r" % is_anagram("Sutha","Sutha")

def has_duplicates(ls):
	"""
		check for duplicate items in the list
	"""
	for li in ls:
		if ls.count(li) > 1:
			return True
		return False
			

#ls = [1,2,3,4,5]
#print has_duplicates(ls)

#ls = ['Sutha', 'sutha', 'SUTHA']
#print has_duplicates(ls)

#ls = ['Sutha', 'Sutha', 'amma']
#print has_duplicates(ls)

#ls = [1,2,3,[1,2], [3,4], 5,6,[1,2]]
#print has_duplicates(ls)

#ls = ['a',['a', 'b'], 'b']
#print has_duplicates(ls)


def random_birthday(n, y1, y2):
	"""
		Generate n number of random birthdays with in give year range
	"""
	bdayls = []
	for i in range(n):
		year = random.randint(y1,y2)
		month = random.randint(1,12)
		day  = random.randint(1,31)
		
		bday = "{0}:{1:02d}:{2:02d}".format(year,month,day)
		print bday
		bdayls.append(bday)
	return bdayls
	
	
	
#bdayls = random_birthday(25, 1880,1985)
#bdayls.sort()
#print bdayls
#print "Bday Dupliactes %r" % has_duplicates(bdayls)


def bisect(ls, li, dosort):
	"""
		Binary Search Algorithm
	"""
	if len(ls) == 0:
		return False
		
	
	if dosort:
		ls.sort()
	n = len(ls)
	print "length %d" % n
	n = int(n/2)
	print "*************************"
	print n
	
	if n == 1:
		return (ls[0] == li)
	
	#print ls
	#print ls[n]
	#print li
	if(ls[n] == li):
		#print " Yes in"
		return True
	
	
	if li > ls[n]:
		ls1 = ls[n:]
		return bisect(ls1, li, False)
	else:
		ls1 = ls[:n]
		return bisect(ls1, li, False)
	print "****************************"
	return False
	

	

def makelist1(filename):
	res =[]
	fin = open(filename)
	for line in fin:
		#print line
		if line.strip() not in res:
			res.append(line.strip())
	print len(res)
	return res
	
	
def makelist2(filename):
	res =[]
	fin = open(filename)
	for line in fin:
		#print line
		if line.strip() not in res:
			res = res + [line]
	print len(res)
	return res
	
def makelist3(filename):
	res = []
	fin = open(filename)
	for line in fin:
		if len(res) < 2:
			res.append(line.strip())
		elif  bisectmine(res, line.strip()) == len(res):
			res.append(line.strip())
	print "List3 %d" % len(res)
	return res
			
	

	
timestart = time.time()
#makelist1("words.txt")
timeend = time.time()

print "timeelapsed1 = %r " % (timeend - timestart)

timestart = time.time()
#makelist2("words.txt")
timeend = time.time()

print "timeelapsed2 = %r" % (timeend- timestart)

timestart = time.time()
#makelist3("words.txt")
timeend = time.time()

#print "timeelapsed3 = %r" % (timeend- timestart)






	
	
ls = [1,22,4,67,78,80,3,5,78,24,5,6,7,8,89,90,100,1000,123,4556,768,4542,25442,1,2,4,5,6,82]
ls1 = ["a", "aah"]
ls1.sort()


def bisectalgo(ls,li):
	ls.sort()
	#print ls
	#print li

	hi = len(ls)
	lo = 0
	org = ls
	while(lo  < hi):
		lst = org[lo:hi]
		#print lst
		mid = (lo + hi)//2
		#print "%d  : %d : %d : %r" %(lo, hi, mid , ls[mid])
		if(ls[mid] > li):
			hi = mid - 1
			#print "hi : %d" % hi
		elif(ls[mid] < li):
			lo = mid + 1
			#print "lo : %d" % lo
		else:
			return mid
	return -1;
	
def bisectmine(ls,li):
	lo = 0
	hi = len(ls)
	while(lo < hi):
		mid = (lo + hi)//2
		if ls[mid] < li:
			lo  = mid + 1
		else:
			hi = mid
	return lo
	
def bisectlib(ls, li):
	i = bisect_left(ls, li)
	if i != len(ls):
		return i
	else:
		return -1
		
		
def makelist4(filename):
	res = []
	fin = open(filename)
	for line in fin:
		i = bisectlib(res, line.strip())
		#print "bisectlib = %d" % i
		if  i == -1:
			res.append(line.strip())
	print "List4 %d" % len(res)
	return res
		
		

#print bisect(ls, 4)
ls.sort()
#print ls
#print bisectalgo(ls,80)

#print ls1
#print bisectalgo(ls1,"aah")

timestart = time.time()
makelist3("words.txt")
timeend = time.time()

print "timeelapsed3 = %r" % (timeend- timestart)


timestart = time.time()
makelist4("words.txt")
timeend = time.time()

print "timeelapsed4 = %r" % (timeend- timestart)

def test1(ls, li):
	if li in ls:
		return True
	return False
		
def test2(ls, li):
	if bisect(ls,li,True):
		return True
	return False
	


#timestart = time.time()
#print test1(ls, 78)
#timeend = time.time()

#print "timeelapsed1 = %r " % (timeend - timestart)

#timestart = time.time()
#print test2(ls,78)
#timeend = time.time()
#print "timeelapsed2 = %r " % (timeend - timestart)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

			
