class Unit:
	
	def __init__(self, health, place = None):
		self.health = health
		self.place = place

	def get_hit(self, damage):
		self.health -= damage

		if self.health <= 0:
			game_print('{0} ran out of armor and expired'.format(self))
			self.place.remove_unit(self)

	def attack(self, hoomans):

	def is_human(self):
		return False


	def __repr__(self):
		name = type(self).__name__
		return '{0}{1}, {2})'.format(name, self.health, self.place)


class Human(Unit):

	cost = 0
	real = False

	def is_human(self):
		return True

	def act(self, campus):

	def get_target(self):
		place = self.place
		while not isinstance(place, Tree):
			if len(place.squirrels) > 0:
				return place.squirrels[0]
			place = place.entrance
		return None

	def attack(self, target):
		target.health -= self.damage

class Undergraduate(Human):

	def act(self, campus):
		self.attack(self.get_target()):

class GSI(Human):

	real = True
	cost = 2
	name = 'GSI'

	def act(self, campus):
		campus.nuts += 1

class Sophomore(Undergraduate):

	cost = 3
	name = 'Sophomore'
	real = True
	damage = 1

	def get_target(self):
		place = self.place
		targets = []
		while not isinstance(place, Tree) and len(targets) < 2:
			if len(place.squirrels) > 0:
				targets += place.squirrels
			place = place.entrance

	def attack(self, target):
		if len(target) <= 2:
			for t in target:
				Human.attack(self, t)
		else:
			target0 = target[0]
			target1 = target[1]
			Human.attack(self, target0)
			Human.attack(self, target1)

class Senior(Sophomore):
	
	cost = 6
	real = True
	damage = 2
	

class Squirrel(Unit):

    name = 'muthafuckin Squirrel'

	def attack(self, Human):
		Human.get_hit(1)

	def move(self, place):
		self.place.remove_unit(self)
        place.add_unit(self)

    def action(self, campus):
        if self.place is not campus.Tree and self.health > 0:
            self.move(self.place.exit)


