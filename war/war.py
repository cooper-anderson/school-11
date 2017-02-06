# Cooper Anderson
# War v1.0.0

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
		self.action = "play"
		self.round = 0

	def play(self):
		if self.check_living:
			if not self.war:
				self.round += 1
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
				self.action = "war"
			else:
				self.currentPlayers = [player.id for player in self.players]
				self.players[self.cards[0].player].win_round(self.cards + self.stack)
				self.cards = []
				self.stack = []
				self.action = "play"

war = War(input("Enter how many players are playing: "), input("Enter the amount of cards you should put down during a war: "))
while True:
	war.play()
	if False in war.cards:
		break
	if war.action == "play":
		print '-' * 16 + "ROUND " + str(war.round) + '-' * 16
		print "".join(["Player " + str(card.player) + " played the " + str(card) + '\n' for card in war.cards])
	if war.action == "war":
		print ' ' * 16 + "WAR" + ' ' * 16
		print ("".join(["Player " + str(player) + " plays a card face down" + '\n' for player in war.currentPlayers]) + '\n') * len(war.currentPlayers)
	print "".join(["Player " + str(war.players[player].id) + " has " + str(war.players[player].card_count()) + " cards left.\n" for player in war.currentPlayers])
	war.check_win()

print "Game ended in " + str(war.round) + " rounds."