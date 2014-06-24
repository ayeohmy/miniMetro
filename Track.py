
# Track node 
# next
# prev
# station itself

class Track:
    def __init__(self, colour):
		self.colour = colour
		self.next = None
		self.prev = None
		self.head = True
		self.tail = True
		self.loop = False

	def isLastStop(self) 
