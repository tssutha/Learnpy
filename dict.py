import string
import random
from bisect import bisect_left
import time

def get_wordmap(filename):
	fin = open(filename)
	wordmap = dict()
	count = 1;
	for line in fin:
		wordmap[str(line.strip())] = count
		count += 1
	return wordmap

def get_wordlist(filename):
	fin = open(filename)
	wordlist = list()
	for line in fin:
		wordlist.append(line.strip())
	return wordlist
		

def is_inwordmap(s):
	wordmap = get_wordmap("words.txt")
	if str(s) in wordmap.keys():
		return True
	else:
		return False
		
def is_inwordlist(s):
	wordlist = get_wordlist("words.txt")
	if s in wordlist:
		return True
	else:
		return False
		
def bisectsearch(ls,s):
	index = bisect_left(ls,s)
	#print index
	if index != len(ls) and ls[index] == s :
		return True
	else:
		return False
		
def is_inwordlistbinser(s):
	wordlist = get_wordlist("words.txt")
	if bisectsearch(wordlist,s):
		return True
	else:
		return False
		
start = time.time()
#res = is_inwordmap("zygoma")
end = time.time()

#print "Dict : res = %r , timeelapsed = %d" % (res, end-start)

start = time.time()
#res = is_inwordlist("zygomaaaa")
end = time.time()

#print "list : res = %r , timeelapsed = %d" % (res, end-start)

start = time.time()
#res = is_inwordlistbinser("zySuthagoma")
end = time.time()

#print "list BisectS : res = %r , timeelapsed = %d" % (res, end-start)

	


def charFrequencyCounter(s):
	"""
		Takes a string as input and returns a dictionary with
		 frequency of each character in the word
	"""
	frqCount = dict()
	s = s.lower()
	for c in s:
		if c not in frqCount:
			frqCount[c] = 1
		else:
			frqCount[c] += 1
	return frqCount
	
	
	
def print_hist(s):
	"""
		Print the histogram of the given word
	"""
	d = charFrequencyCounter(s)
	keylist = d.keys()
	
	keylist.sort()
	for k in keylist:
		print "%r : %d" % (k, d[k])
		
#print_hist("Suthakaran")
#print charFrequencyCounter("Suthakaran")
		



def fibonacci(n):
	"""
		fibonacci with recursion
	"""
	if n == 0:
		return 0
	if n == 1:
		return 1
		
	return fibonacci(n-1) + fibonacci(n-2)
	
known = {0:0, 1:1}
def fibonacci_with_dict(n):
	"""
		fibonacci series with use of dictionary
	"""
	if n in known:
		return known[n]
	
	res = fibonacci_with_dict(n-2) + fibonacci_with_dict(n-1)
	known[n] = res
	return res
	


start = time.time()
#print fibonacci(30)
end = time.time()

#print "Dict : res = %r , timeelapsed = %f" % (0, end-start)

start = time.time()
#print fibonacci_with_dict(30)
end = time.time()

#print "list : res = %r , timeelapsed = %f" % (0, end-start)


def sort_by_length(words):
	"""
		sort words by their length
	"""
	t =[]
	for word in words:
		t.append((len(word),random.random(),word))
	res = []
	t.sort(reverse = False)
	
	for length,ran, word in t:
		res.append(word)
	return res
	
words = ['sutha','Sutha','aruntha','ammaaa','chevanthi', 'singapore', 'lankna']

#res = sort_by_length(words)

#for s in res:
#	print s
		

def char_frequency(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
			
	res = []
	for c,n in d.items():
		res.append((n,c))
	
	res.sort(reverse=True)

	return res;

#print char_frequency('ssssuyyyuuuuuuuuuttthtaaaakkkaran')
			
		
def is_anagram(s1,s2):
	if(len(s1)!=len(s2)):
		return False
	for c in s1:
		if(s1.count(c) != s2.count(c)):
			return False;
	return True
	
def make_wordlist(filename):
	fin = open(filename)
	res = []
	for line in fin:
		res.append(line.strip())
	return res
	
def find_anagram_set(filename):
	wordlist = make_wordlist(filename)
	finalres = []
	checkedword = []
	count  =0
	for word in wordlist:
		word = word.lower()
		ls = list(word)
		ls.sort()
		word = ''.join(ls)
		count += 1
		print word, count
		if word not in checkedword:
			checkedword.append(word)
			tempwordlist = wordlist
			#tempwordlist.remove(word)
			res_list = []
			#res_list.append(word)
			for word2 in tempwordlist:
				word2.lower()
				if  is_anagram(word,word2):
					res_list.append(word2)
			if(len(res_list)>1):
				finalres.append(res_list)
	return finalres
			
				
#print find_anagram_set('words.txt')	

def get_signature(word):
	word = word.lower()
	ls = list(word)
	ls.sort()
	word = ''.join(ls)
	return word

#print get_signature('sutha')

word_dict = {}

def get_worddictionary(filename):
	fin = open(filename)
	for line in fin:
		line = line.strip()
		signature = get_signature(line)
		if signature not in word_dict:
			word_dict[signature] = [line]
		else:
			word_dict[signature].append(line)
			
def print_all_anagrams():
	count = 0
	for k,v in word_dict.items():
		if len(v) > 1:
			count += 1
			print "%r : %d" %(v,count)
			
#get_worddictionary('words.txt')
#print_all_anagrams()
	
def calculate_dist(word1, word2):
	assert len(word1) == len(word2)
	count = 0
	for c1, c2 in zip(word1,word2):
		if c1 != c2:
			count += 1
	return count
		
def get_all_metathesis():
	count = 0
	for v in word_dict.values():
		for wd1 in v:
			for wd2 in v:
				if calculate_dist(wd1,wd2) == 2 :
					count += 1
					print "[%s] , [%s], [%d]" % (wd1,wd2,count)	


#get_all_metathesis()

def remove_punctuation_whitespace(line):
	line.strip()
	ls = line.split()
	res =  []
	for n in range(len(ls)):
		lsword = list(ls[n])
		templist = lsword
		for i in range(len(lsword)):
			if lsword[i] in string.punctuation:
				templist.remove(lsword[i])
		word = ''.join(templist)
		res.append(word)
	return res
			

def get_all_words(filename):
	fin = open(filename)
	wordlist = []
	for line in fin:
		line = line.strip()
	    #line = ''.join(ch for ch in line if ch not in string.punctuation)
	    ls = list("")
	    for ch in line:
	    	if ch not in string.punctuation:
	    		ls.append(ch)
	    line = ''.join(ls)
	    		
		wordlist.extend(line.split(" "))
	return wordlist

print get_all_words('test.txt')		


















	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
