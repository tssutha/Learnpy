import string
import random
from bisect import bisect_left
import os

def process_line(line, histo):
	line = line.replace("_", " ")
	for word in line.split():
		word = word.strip(string.whitespace + string.punctuation)
		word = word.lower()
		histo[word] = histo.get(word,0) + 1
	 
	
	
def process_file(filename):
	fin = open(filename)
	histo = dict()
	for line in fin:
		process_line(line,histo)
	return histo

histo = process_file('test1.txt')

def get_total_words(histo):
	return sum(histo.values())

#print get_total_words(histo)

def get_most_freq_word(histo, n):
	wordhisto = []
	for k,v in histo.items():
		wordhisto.append((v,k))
	
	wordhisto.sort(reverse = True)
	return wordhisto[0:n]
	
	
ls = get_most_freq_word(histo, 10)
for i in range(len(ls)):

	count, word = ls[i]
	print "Word : %r  Count : %d" % (word,count)


ls =  histo.values()
#ls.sort()
#print ls



#print ls1[len(ls1) -1]

def get_random_word(histo):
	wordlist = histo.keys()
	lsAccuSum = [0]
	for v in histo.values():
		lsAccuSum.append(lsAccuSum[len(lsAccuSum)-1] + v)
	
	totalnumofwords = lsAccuSum[len(lsAccuSum) - 1]
	lsAccuSum = lsAccuSum[1::]
	rndnum = random.randint(1,totalnumofwords)
	index = bisect_left(lsAccuSum,rndnum)
	return wordlist[index]
	 
	
#print get_random_word(histo)

#print os.getcwd()













	