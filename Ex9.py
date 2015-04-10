from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()


def square(t, length):
	""" Draw Rectangle """
	for i in range(4):
		fd(t,length)
		lt(t)
		
def polygon(t, length, n):
	"""Draw a Polygon"""
	angle = 360/n;
	for i in range(n):
		#lt(t,angle)
		fd(t,length)
		lt(t,angle)
		
def circle(t, r, n):
	"""Draw a Circle"""
	circu = 2 * math.pi * r;
	print circu
	if(n > int(circu/3) + 1):
		n = int(circu/3) + 1
	print n;
	length = circu/n
	polygon(t, length, n)
	
	
bob.delay = 0.0001

#square(bob, 200)
#square(bob, 50)

#polygon(bob, 50, 9)
circle(bob,20,100)

wait_for_user()
	