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
		self.attack(self.get_target()):

	def get_target(self):
		place = self.place
		while not isinstance(place, Tree):
			if len(place.squirrels) > 0:
				return place.squirrels[0]
			place = place.entrance
		return None

	def attack(self, target):
		if target is not None:
			target.get_hit(self.damage)

class GSI(Human):

	real = True
	cost = 2
	name = 'GSI'

	def act(self, campus):
		campus.nuts += 1

class Freshman(Human):
    name = 'Freshman'
    real = True
    damage = 1
    cost = 2

class Junior(Human):
    name = 'Junior'
    real = True
    damage = 3
    cost = 4

class Sophomore(Human):

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
		if len(target) = 0:
			return
		elif len(target) = 1:
			Human.attack(self, target)
		else:
			target0 = target[0]
			target1 = target[1]
			Human.attack(self, target0)
			Human.attack(self, target1)

class Senior(Sophomore):

	name = 'Senior'
	cost = 6
	real = True
	damage = 2

class CSProfessor(Human):

	name = 'CS Professor'
	cost = 6
	damage = 0
	prof_exists = False
	line = 'I am a computer scientist!'

	def __init__(self, health, place=None):
		if not CSProfessor.prof_exists:
			Unit.__init__(self, health, place)
			CSProfessor.prof_exists = True
		else:
			return

	def act(self, campus):
		self.talk_shit()

	def talk_shit(self):
		# print(self.line)
		self.get_hit(self.health)

class Hilfinger(CSProfessor):

	name = 'Hilfinger'
	real = True
	line = 'RTFM!'

	def act(self, campus):
		Senior.damage *= 2
		Junior.damage *= 2
		Sophomore.damage *= 2
		Freshman.damage *= 2
		place = self.place.entrance
		while not isinstance(place, Tree):
			if place.Human:
				place.Human.damage *= 2
			place = place.entrance
		place = self.place.exit
		while not isinstance(place, Nuts):
			if place.Human:
				place.Human.damage *= 2
			place = place.exit
		CSProfessor.act(self, campus)

class DeNero(CSProfessor):

	name = 'DeNero'
	real = True
	line = ' '

	def act(self, campus):
		place = self.place.exit
		while not isinstance(place, Nuts):
			place = place.exit
		while not isinstance(place, Tree):
			place.Squirrels = []
			place = place.entrance
		CSProfessor.act(self, campus)

class Hug(CSProfessor):

	name = 'Hug'
	real = True
	line = ' '
	hugs = 0
	
	def __init__(self, health, place=None):
		if not CSProfessor.prof_exists or Hug.hugs < 3:
			Unit.__init__(self, health, place)
			CSProfessor.prof_exists = True
			Hug.hugs +=1
		else:
			return

	def act(self, campus):
		place = self.place.exit
		length = 5
		while not isinstance(place, Nuts):
			place = place.exit
		while not isinstance(place, Tree) and length > 0:
			place.Squirrels = []
			place = place.entrance
			length -= 1
		CSProfessor.act(self, campus)
	

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


