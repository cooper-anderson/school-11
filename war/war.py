# Cooper Anderson
# War v0.1.0-beta0

from cards import Card, Deck
import random, time


class Player(object):
	def __init__(self, id=0, cards=[]):
		self.id = id
		self.score = 0
		self.hand = cards
		self.pile = []

	def card_count(self):
		return len(self.hand + self.pile)

	def play_card(self):
		if not self.card_count():
			return False
		else:
			if not len(self.hand):
				random.shuffle(self.pile)
				self.hand = self.pile
				self.pile = []
			self.hand[0].player = self.id
			return self.hand.pop(0)

	def win_round(self, cards):
		self.pile += cards;
		self.score += len(cards)


class War(object):
	def __init__(self, players=2, warCount=3):
		deck = Deck().shuffle()
		self.players = [Player(p, deck.pop(52 / players)) for p in range(players)]
		self.currentPlayers = [p.id for p in self.players]
		self.cards = []
		self.stack = []
		self.warCount = warCount
		self.war = 0

	def play(self):
		if self.check_living:
			if not self.war:
				self.cards = []
				for p in self.currentPlayers:
					self.cards.append(self.players[p].play_card())
			else:
				for p in self.currentPlayers:
					self.stack.append(self.players[p].play_card())
				self.war -= 1
			return True
		return False

	def check_living(self):
		for player in self.players:
			if not player.card_count():
				return False
		return True

	def check_win(self):
		if False not in self.cards and len(self.cards):
			self.cards.sort()
			self.cards.reverse()
			self.check_war(self.cards)

	def check_war(self, cards):
		if len(self.cards):
			wars = 0
			firstCard = cards[0]
			for card in cards[1:]:
				if card == firstCard:
					wars += 1
				else:
					break
			if wars:
				self.currentPlayers = [self.cards[c].player for c in range(wars + 1)]
				self.stack += self.cards
				self.cards = []
				self.war = self.warCount - 1
			else:
				self.currentPlayers = [player.id for player in self.players]
				self.players[self.cards[0].player].win_round(self.cards + self.stack)
				self.cards = []
				self.stack = []

war = War(8)
while False not in war.cards:
	war.play()
	print war.cards
	print [player.card_count() for player in war.players]
	war.check_win()
