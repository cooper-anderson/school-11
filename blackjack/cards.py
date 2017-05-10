# Cooper Anderson
# Cards v0.2.0-beta0

from copy import deepcopy
import random
import pyglet.image as image


class Suit(object):
	def __init__(self, name="Hearts", index=0):
		self.name = name
		self.index = index

	def __eq__(self, other):
		return True if self.index == other.index else False

	def __str__(self):
		return self.name

	def __repr__(self):
		return str(self.index)


class Rank(object):
	def __init__(self, name="2", abbr="2", rank=2, order=0):
		self.name = name
		self.abbr = abbr
		self.rank = rank
		self.order = order

	def __eq__(self, other):
		if type(other) == int:
			return True if self.rank == other else False
		return True if self.rank == other.rank and self.order == other.order else False

	def __gt__(self, other):
		if self.rank == other.rank:
			return self.order > other.order
		return self.rank > other.rank

	def __lt__(self, other):
		if self.rank == other.rank:
			return self.order < other.order
		return self.rank < other.rank

	def __str__(self):
		return self.name

	def __repr__(self):
		return str(self.rank)

suits = [Suit("Spades", 0), Suit("Hearts", 1), Suit("Clubs", 2), Suit("Diamonds", 3)]
ranks = [
	None,
	None,
	Rank('2', '2', 2),
	Rank('3', '3', 3),
	Rank('4', '4', 4),
	Rank('5', '5', 5),
	Rank('6', '6', 6),
	Rank('7', '7', 7),
	Rank('8', '8', 8),
	Rank('9', '9', 9),
	Rank("10", 'X', 10),
	Rank("Jack", 'J', 11, 0),
	Rank("Queen", 'Q', 11, 1),
	Rank("King", 'K', 11, 2),
	Rank("Ace", 'A', 12)
]


class Card(object):
	def __init__(self, suit=0, rank=2):
		self.suit = suits[suit]
		self.rank = ranks[rank]
		self.image = image.load("cards/" + str(self.rank) + "_of_" + str(self.suit) + ".png")

	def draw(self, x=0, y=0, scale=1):
		self.image.blit(x, y, 0)

	def __eq__(self, other):
		return True if self.rank == other.rank else False

	def __gt__(self, other):
		return self.rank > other.rank

	def __lt__(self, other):
		return self.rank < other.rank

	def __str__(self):
		return str(self.rank) + " of " + str(self.suit)

	def __repr__(self):
		return '<' + str(self) + '>'

cards = [Card(suit, rank) for suit in range(len(suits)) for rank in range(len(ranks)) if rank not in [0, 1]]


class Deck(object):
	def __init__(self, player=0, empty=False):
		self.cards = deepcopy(cards) if not empty else []
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
		cycled_cards = self.pop(count)
		self.cards += cycled_cards
		return cycled_cards
