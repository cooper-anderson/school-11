# Cooper Anderson
# Monster class


class Monster(object):
	def __init__(self):
		self.health = 0
		self.maxHealth = 0
		self.stamina = 0
		self.maxStamina = 0
		self.stealth = 0
		self.intelligence = 0
		self.stal = False

# Basic Monsters


class Bokoblin(Monster):
	def __init__(self):
		pass


class Moblin(Monster):
	def __init__(self):
		pass


class Lizalfos(Monster):
	def __init__(self):
		pass


class Chuchu(Monster):
	def __init__(self):
		pass


class Octorok(Monster):
	def __init__(self):
		pass


class Keese(Monster):
	def __init__(self):
		pass


class Wizzrobe(Monster):
	def __init__(self):
		pass


class Pebblit(Monster):
	def __init__(self):
		pass

# Special Monsters


class Hinox(Monster):
	def __init__(self):
		pass


class Molduga(Monster):
	def __init__(self):
		pass


class Talus(Monster):
	def __init__(self):
		pass


class Lynel(Monster):
	def __init__(self):
		pass

# Bokoblin Variations


# Basic Stal Monsters


class Stalkoblin(Bokoblin):
	def __init__(self):
		self.stal = True


class Stalmoblin(Moblin):
	def __init__(self):
		self.stal = True


class Stalfos(Lizalfos):
	def __init__(self):
		self.stal = True

# Special Stal Monsters


class Stalnox(Hinox):
	def __init__(self):
		self.stal = True
