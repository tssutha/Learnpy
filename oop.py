import string
import math
import copy

class Point(object):
	def __init__(self):
		self.x = 0.0
		self.y = 0.0
	
	def setcoord(self, x, y):
		self.x = x
		self.y = y
		
	def dist_btwn_points(self, pt1, pt2):
		dist = math.sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)
		return dist
	
		
class Rectangle(object):
	def __init__(self, pt,width, height):
		self.x = pt.x
		self.y = pt.y
		self.width = width
		self.height = height
	
	def get_center_point(self):
		centPt = Point()
		centPt.x = self.x + self.width /2.0
		centPt.y = self.y + self.height /2.0
		return centPt
	
	def move_rect_to(self, pt):
		self.x = pt.x
		self.y = pt.y
		
		
pt = Point()
pt.setcoord(10.0,20.0)

pt1 = Point()
pt1.setcoord(5.0,10.0)



#print pt.dist_btwn_points(pt,pt1)

rect = Rectangle(pt,100,200)
cpt = rect.get_center_point()

rect.move_rect_to(pt1)
cpt = rect.get_center_point()

rect1  = rect
#print rect1 == rect

#print rect is rect1

#rect1  = copy.copy(rect)

#print rect1 is rect


class Time(object):
	def __init__(self):
		self.hour = 0
		self.min  = 0
		self.sec  = 0
		
	def add(self, t):
		self.hour += t.hour
		self.sec  += t.sec
		if self.sec >=60:
			self.sec -= 60
			self.min += 1
		
		self.min += t.min
		if self.min >= 60:
			self.min -= 60
			self.hour += 1
		
		if self.hour >= 24:
			self.hour -= 24
			
			
		newtime = Time()
		newtime.hour = self.hour
		newtime.min = self.min
		newtime.sec = self.sec
		return newtime
		
t = Time()
t.hour = 8
t.min  = 20
t.sec  = 56

t1 = Time()
t1.hour = 8
t1.min  = 54
t1.sec  = 10

t = t.add(t1)
print t

print "%.2d:%.2d:%.2d" % (t.hour, t.min,t.sec)










		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	