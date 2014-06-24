class Station:
	def __init__(self, shape):
		self.shape = shape
		self.connected = False
		self.passengers = []
		self.stationSize = 6
		self.next = None
		self.prev = None

	def waiting(self):
		return len(self.passengers)