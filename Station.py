class Station:
	def __init__(self, shape):
		self.shape = shape
		self.connected = False
		self.passengers = []
		self.stationSize = 6

	def waiting(self):
		return len(self.passengers)