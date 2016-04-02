class Unit:
	def __init__(self, place, name):
		self.place = place
		self.name = name
	def __repr__(self):
		return self.name
class Human(Unit):
	def __init__(self, place, name, health, damage):
		Unit.__init__(self, place, name)
		self.health = health
		self.damage = damage
	def lose_health(self, hit=1):
		self.health -= hit
		if self.health <= 0:
			self.remove_unit()
	def remove_unit(self)