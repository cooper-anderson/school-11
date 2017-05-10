# Cooper Anderson
# Blackjack v0.1.0-beta0

from __future__ import print_function
from cards import Deck
from collections import defaultdict
import pyglet
from pyglet.window import key


class Hand(Deck):
	def __init__(self, id=0):
		super(self.__class__, self).__init__(id, True)

	def get_total(self):
		self.cards += [self.cards.pop(i) for i, card in enumerate(self.cards) if card.rank == 12]
		score = 0
		for card in self.cards:
			if card.rank == 11:
				score += 10
			elif card.rank == 12:
				score += 11 if score < 11 else 1
			else:
				score += card.rank.rank
		return score


class Player(object):
	def __init__(self, id=0):
		self.id = id
		self.hand = Hand(self.id)
		self.score = 5000

	def get_total(self):
		return self.hand.get_total()


class Blackjack(object):
	def __init__(self):
		self.deck = Deck(0)
		self.deck.shuffle()
		self.pile = Deck(0, True)
		self.hand = Hand(0)
		self.player = Player(1)
		self.hide_card = True

	def hand_card(self):
		if not len(self.deck.cards):
			self.deck = self.pile.shuffle()
			self.pile = Deck(0, True)
		return self.deck.pop()

	def deal(self):
		for i in range(2):
			self.player.hand.cards.append(self.hand_card())
			self.hand.cards.append(self.hand_card())

	def round(self):
		self.deal()
		print("Dealer: (", end='')
		if self.hide_card:
			if self.hand.cards[0].rank.rank < 11:
				print(self.hand.cards[0].rank, end='')
			elif self.hand.cards[0].rank.rank < 12:
				print(10, end='')
			else:
				print(11, end='')
		else:
			print(str(self.hand.get_total()),)
		print(")")
		if self.hide_card:
			print("  " + str(self.hand.cards[0]) + "\n  ???\n")
		else:
			'\n'.join(["  " + str(card) for card in self.hand.cards]) + '\n'
		print("Your hand: (" + str(self.player.get_total()) + ")\n" + '\n'.join(["  " + str(card) for card in self.player.hand.cards]) + '\n')

	def play(self, entry):
		if 'h' in entry.lower():
			pass
		elif 's' in entry.lower():
			pass

window = pyglet.window.Window()
title_text = pyglet.text.Label("Blackjack", x=275, y=450)
dealer_text = pyglet.text.Label("Dealer Hand:", x=10, y=400)
player_text = pyglet.text.Label("Player Hand:", x=10, y=250)
instructions_text = pyglet.text.Label("Press H to hit / S to stand", x=255, y=50)
keys = defaultdict(lambda: 0)
blackjack = Blackjack()
blackjack.deal()


def draw_cards(cards=[], x=10, y=10, width=100):
	for index, card in enumerate(cards):
		card.draw(x + (width*index), y)


@window.event
def on_key_press(symbol, modifiers):
	keys[symbol] = 2


@window.event
def on_key_release(symbol, modifiers):
	keys[symbol] = 0


def update_keys():
	for index in keys:
		keys[index] = 1 if keys[index] == 2 else keys[index]


def update(dt):
	if keys[key.H] == 2:
		blackjack.player.hand.cards.append(blackjack.hand_card())
	update_keys()


@window.event
def on_draw():
	window.clear()
	title_text.draw()
	dealer_text.draw()
	player_text.draw()
	instructions_text.draw()
	draw_cards(blackjack.player.hand.cards, 10, 125)

# pyglet.clock.schedule_once(start, 0)
pyglet.clock.schedule(update)

pyglet.app.run()

"""while True:
	blackjack = Blackjack()
	print('\n' * 100)
	blackjack.round()
	while True:
		blackjack.play(raw_input("What would you like to do? (hit, stand): "))"""
