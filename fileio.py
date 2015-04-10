import string
import os
from os.path import getsize, join
import urllib

def get_dir_info(dirname):
	for name in os.listdir(dirname):
		name = os.path.join(dirname,name)
		if os.path.isfile(name):
			print name
		else:
			get_dir_info(name)
			
#get_dir_info('../hackercircle')


def get_dir_info_1(dirname):
	for root, dirs, files in os.walk(dirname):
		print root
		print dirs
		print files
		
def get_dir_info_2(dirname):
	for root, dirs, files in os.walk(dirname):
		print root, "concumes"
		print sum(getsize(join(root,file)) for file in files),
		print "bytes in", len(files) ,"files"
	
#get_dir_info_2('../hackercircle')

def read_file(filename):
	if os.access(filename, os.R_OK):
		with open(filename) as fp:
			return fp.read()
	return "some default data"
	
def read_file_safe(filename):
	try:
		fp = open(filename)
	except IOError as e:
		if e.errno == os.errno.EACCES:
			return "some default data"
		raise
	else:
		return fp.read()

#print read_file_safe("test.txt")

def get_updatedfile(filesrc, filedes, pattern, replacement):
	try:
		contents = ""
		with open(filesrc) as fpsrc:
			contents = fpsrc.read()
		contents = contents.replace(pattern,replacement)
		
		with open(filedes, 'w+') as fpdes:
			fpdes.write(contents)
	except:
		print "Some File is not correct"
		return -1
	else:
		return 0
	
#get_updatedfile("test.txt", "test1.txt", " the ", "sutha")


def read_secret():
	conn = urllib.urlopen('http://thinkpython.com/secret.html')
	for line in conn:
		print line.strip()
	conn.close()
	
	
read_secret()	
	
	
	
	
	
	
	
	
	
	
	