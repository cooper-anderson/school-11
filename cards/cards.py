# Cooper Anderson
# Cards v0.1.5

from copy import deepcopy
import random

class Suit(object):
	def __init__(self, name=""):
		self.name = name

	def __eq__(self, other):
		return self.name == other.name


class Rank(object):
	def __init__(self, rank="", value=0, priority=0, face=False, abbreviation=""):
		self.rank = rank
		self.value = value
		self.priority = priority
		self.face = face
		self.abbreviation = rank if abbreviation == "" else abbreviation

	def __eq__(self, other):
		return self.value == other.value and self.priority == other.priority

	def __gt__(self, other):
		if self.value == other.value:
			return self.priority > other.priority
		return self.value > other.value

	def __lt__(self, other):
		if self.value == other.value:
			return self.priority < other.priority
		return self.value < other.value

suits = [Suit("Hearts"), Suit("Clubs"), Suit("Diamonds"), Suit("Spades")]
ranks = [
	Rank("Ace", 12, 0, False, 'A'), Rank('2', 2), Rank('3', 3), Rank('4', 4), Rank('5', 5), Rank('6', 6), Rank('7', 7), Rank('8', 8), Rank('9', 9), Rank('10', 10, 0, False, 'X'), Rank("Jack", 11, 0, True, 'J'), Rank("Queen", 11, 1, True, 'Q'), Rank("King", 11, 2, True, 'K')
]


class Card(object):
	suits = suits
	ranks = ranks

	def __init__(self, suit=suits[0], rank=ranks[0], player=0):
		self.suit = suit
		self.rank = rank
		self.player = player

	def get_name(self):
		return self.rank.rank + " of " + self.suit.name

	def get_abbr(self):
		return self.rank.abbreviation + self.suit.name[0]

	def __eq__(self, other):
		try: return self.rank == other.rank
		except AttributeError: return False

	def __gt__(self, other):
		return self.rank > other.rank

	def __lt__(self, other):
		return self.rank < other.rank

	def __str__(self):
		return self.get_name()

	def __repr__(self):
		return '<' + self.get_name() + '>'

cards = [Card(suit, rank) for suit in suits for rank in ranks]


class Deck(object):
	def __init__(self, player=0):
		self.cards = [Card(suit, rank, player) for suit in suits for rank in ranks]
		self.player = player

	def shuffle(self):
		random.shuffle(self.cards)
		return self

	def pop(self, count=1):
		if count == 1:
			return self.cards.pop(0)
		else:
			popped = []
			for i in range(count):
				popped.append(self.pop())
			return popped

	def cycle(self, count=1):
		cycledCards = self.pop(count)
		self.cards += cycledCards
		return cycledCards
