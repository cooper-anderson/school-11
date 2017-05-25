#!/usr/bin/env python
# Cooper Anderson
# Blackjack v0.1.0-beta0

from __future__ import print_function
from cards import Deck
from collections import defaultdict
import pyglet
from pyglet.window import key
from copy import deepcopy

class Hand(Deck):
	def __init__(self, id=0):
		super(self.__class__, self).__init__(id, True)

	def get_total(self):
		cards = deepcopy(self.cards)
		cards += [cards.pop(i) for i, card in enumerate(cards) if card.rank == 12]
		score = 0
		for card in cards:
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
		self.standing = False
		self.playing = True
		self.hasBlackjack = False
		self.hasBusted = False

	def get_total(self):
		return self.hand.get_total()


class Blackjack(object):
	def __init__(self):
		self.deck = Deck(0)
		self.deck.shuffle()
		self.pile = Deck(0, True)
		self.hand = Hand(0)
		self.hand.hasBlackjack = False
		self.hand.hasBusted = False
		self.player = Player(1)

	def hand_card(self):
		if not len(self.deck.cards):
			self.deck = self.pile.shuffle()
			self.pile = Deck(0, True)
		return self.deck.pop()

	def deal(self):
		for i in range(2):
			self.player.hand.cards.append(self.hand_card())
			self.hand.cards.append(self.hand_card())

	def play_dealer(self):
		while self.hand.get_total() < 17:
			self.hand.cards.append(self.hand_card())
		dealer_total = self.hand.get_total()
		if dealer_total == 21:
			self.hand.hasBlackjack = True
		elif dealer_total > 21:
			self.hand.hasBusted = True

	def round(self):
		player_total = self.player.hand.get_total()
		if player_total == 21:
			self.player.playing = False
			self.player.hasBlackjack = True
		elif player_total > 21:
			self.player.playing = False
			self.player.hasBusted = True
		if not self.player.playing:
			self.play_dealer()

	def play(self, entry):
		if 'h' in entry.lower():
			if self.player.playing:
				blackjack.player.hand.cards.append(blackjack.hand_card())
		elif 's' in entry.lower():
			self.player.standing = True
			self.player.playing = False

window = pyglet.window.Window()
title_text = pyglet.text.Label("Blackjack", x=275, y=450)
dealer_text = pyglet.text.Label("Dealer Hand:", x=10, y=400)
player_text = pyglet.text.Label("Player Hand:", x=10, y=250)
instructions_text = pyglet.text.Label("Press H to hit / S to stand", x=255, y=50)
card_back = pyglet.image.load("cards/card_back.png")
keys = defaultdict(lambda: 0)
blackjack = Blackjack()
blackjack.deal()

def reset():
	global blackjack
	title_text.text = "Blackjack"
	dealer_text.text = "Dealer Hand:"
	player_text.text = "Player Hand:"
	instructions_text.text = "Press H to hit / S to stand"
	blackjack = Blackjack()
	blackjack.deal()

def draw_cards(cards=[], x=10, y=10, hidden=False, width=100):
	for index, card in enumerate(cards):
		if index != 0 or not hidden:
			card.draw(x + (width*index), y)
		else:
			card_back.blit(x + (width*index), y)


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
		blackjack.play("hit")
		# blackjack.player.hand.cards.append(blackjack.hand_card())
	if keys[key.S] == 2:
		blackjack.play("stand")
	if keys[key.R] == 2:
		reset()
	blackjack.round()
	player_text.text = "Player Hand: " + str(blackjack.player.hand.get_total())
	dealer_text.text = "Dealer Hand: " + ('?' if blackjack.player.playing else str(blackjack.hand.get_total()))
	if blackjack.player.hasBusted and blackjack.hand.hasBusted:
		instructions_text.text = "You both bust! Tie!"
	elif blackjack.player.hasBusted:
		instructions_text.text = "You busted! You lose!"
	elif blackjack.hand.hasBusted:
		instructions_text.text = "Dealer busted! You win!"
	elif blackjack.hand.hasBlackjack:
		instructions_text.text = "Dealer has blackjack! You lose!"
	elif blackjack.player.hasBlackjack:
		instructions_text.text = "Blackjack! You win!"
	elif blackjack.player.standing:
		instructions_text.text = "You win!" if blackjack.player.hand.get_total() > blackjack.hand.get_total() else "You lose!"
	update_keys()


@window.event
def on_draw():
	window.clear()
	title_text.draw()
	dealer_text.draw()
	player_text.draw()
	instructions_text.draw()
	draw_cards(blackjack.hand.cards, 10, 275, blackjack.player.playing)
	draw_cards(blackjack.player.hand.cards, 10, 125)

print("Blackjack Starting")

pyglet.clock.schedule(update)

pyglet.app.run()

