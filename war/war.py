# Cooper Anderson
# War v0.1.0-beta0

from cards import Card, Deck
import time


class Player(object):
	def __init__(self, id=0, shuffle=True):
		self.id = id
		self.score = 0
		self.deck = Deck(self.id)
		self.lastPlay = Card()
		if shuffle:
			self.deck.shuffle()

	def play(self):
		self.lastPlay = self.deck.pop()
		return self.lastPlay


class War(object):
	def __init__(self, players=2, warCount=3):
		self.players = [Player(p) for p in range(players)]
		self.cards = []
		self.stack = []
		self.warredPlayers = []
		# self.scores = [0 for p in range(players)]
		self.warCount = warCount
		self.war = 0

	def play(self):
		if not self.war:
			self.stack = []
			self.warredPlayers = []
			self.cards = []
			for player in self.players:
				if len(player.deck.cards):
					self.cards += [player.play()]
			self.cards.sort()
			self.cards.reverse()
			self.check_war(self.cards)
		elif self.war == 1:
			self.war -= 1
			self.check_war(self.cards)
		else:
			for p in self.warredPlayers:
				player = self.players[p]
				if len(player.deck.cards):
					self.stack += [player.play()]
		print [card.get_abbr() for card in self.cards]

	def check_war(self, cards):
		wars = 1
		card = cards[0]
		for i in range(1, len(cards)):
			if card == cards[i]:
				wars += 1
			else:
				break
		if wars > 1:
			self.war = warCount + 1
			self.warredPlayers = [cards[c].player for c in range(wars)]
