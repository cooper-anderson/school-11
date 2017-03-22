# Cooper Anderson
# Monster Battle v0.1.0-beta0

import random


class Weapon(object):
	def __init__(self):
		self.damage = 0

	def get_damage(self):
		return self.damage


class Sword(Weapon):
	def __init__(self):
		Weapon.__init__(self)
		self.damage = 4


class Club(Weapon):
	def __init__(self):
		Weapon.__init__(self)
		self.damage = 5


class Monster(object):
	def __init__(self):
		self.strength = random.randint(3, 18)
		# self.speed = random.randint(3, 18)
		self.dexterity = random.randint(3, 18)
		self.health = random.randint(5, 20)
		self.weapon = False

	def is_alive(self):
		return self.health > 0

	def hurt(self, damage):
		self.health = max(self.health - damage, 0)

	def attack(self, target):
		hit_roll = random.randint(0, 20)
		if self.dexterity >= hit_roll:
			target.hurt(self.weapon.get_damage() * (self.strength / 20.0))
			# target.health -= self.weapon.get_damage() * (self.strength / 20.0)
			return True
		return False


class Hobbit(Monster):
	def __init__(self):
		Monster.__init__(self)
		self.strength -= 1
		self.dexterity += 3
		self.health += 2
		self.weapon = Sword()


class Orc(Monster):
	def __init__(self):
		Monster.__init__(self)
		self.strength += 1
		self.dexterity -= 2
		self.health += 3
		self.weapon = Club()


hobbitCount = 0
orcCount = 0

for i in range(100):

	orc = Orc()
	hobbit = Hobbit()

	while hobbit.is_alive() and orc.is_alive():
		hobbit.attack(orc)
		orc.attack(hobbit)

	if hobbit.is_alive():
		hobbitCount += 1
	else:
		orcCount += 1

print "hobbit wins: ", hobbitCount
print "orc wins: ", orcCount
