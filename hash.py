
class LinearMap(object):
	def __init__(self):
		self.items = []
	
	def add(self, k, v):
		self.items.append((k,v))
	
	def get(self, k):
		for key, val in self.items:
			if key == k:
				return val
		return KeyError


if __name__ == "__main__":
	lmap = LinearMap()
	lmap.add(10,'s')
	lmap.add(20, '2')
	
	print lmap.get(20)