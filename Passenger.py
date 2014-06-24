class Passenger:
	def __init__(self, shape):
		self.dest = shape
		self.path = []
		self.hasPath = false; # but if the game dynamically changes, the path may not be valid anymore