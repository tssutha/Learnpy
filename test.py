import math
import time

l = list()
def reverse(ls):
	#l = list()
	print ls
	l.append(ls[len(ls)-1])
	print l
	if(len(ls)>1):
		reverse(ls[:-1])
	else:
		return l;
	
ls = [1,2,3]

def reverse2(ls):
	if len(ls)>1:
		return reverse2(ls[1:]).append(ls[0])
	else:
		return ls

#print reverse2(ls)

ls = [2, [5,False,[7,False,False]],[9,False,False]]

lastIndex = 0


def issqu(ls, N):
	global lastIndex
	i = lastIndex
	print i
	ln = len(ls)
	while(i < ln and ln >1):
		element = ls[i]
		if element != 'Fizz' :
			if element**2 == N :
				lastIndex = i
				return True
		i = i +1
	return False
		

def fizz(N):
	ls = []
	lastFizz = 0
	for i in range(N):
		if N >= lastFizz:
			if issqu(ls, i+1) == True :
				ls.append('Fizz')
				lastFizz = (math.sqrt(i+1) + 1)**2
			else:
				ls.append(i+1)
			
		else:
			ls.append(i+1)
	return ls
	

def fizz1(N):
	ls = []
	lastFizz = 0
	for i in range(N):
		if issqu(ls, i+1) == True :
			ls.append('Fizz')
			
			
		else:
			ls.append(i+1)
	return ls
	
	
start = time.time()
#print fizz(100)
end = time.time()

print end - start

start = time.time()
print fizz1(100)
end = time.time()

print end - start
	
	
	
	
	
	
	
	
	
	
	