# Cooper Anderson
# Key Visualizer v0.1.3

import pyglet, random, sys

from pyglet.gl import *
from pyglet import font
from pyglet import graphics
from pyglet import window

import particles

window = pyglet.window.Window(resizable=True)
letters = []
keys = {}
keyDelay = 0
globalKeyDelay = 3
space = False
useColors = False
flickerColors = False
useParticles = True
particleCount = 10
help = pyglet.text.Label("1: Toggle Colors\n2: Toggle Color Flicker\n3: Toggle Particles", font_name="Source Code Pro", x=0, y=window.height-24, anchor_x="left", multiline=True, width=window.width)
showHelp = False
message = pyglet.text.Label("Press keys or command", font_name="Source Code Pro", font_size=24, x=window.width//2, y=3*window.height//4, anchor_x="center", anchor_y="center")
messages = ["Toggled Colors", "Toggled Color Flickering", "Toggled Particles"]


class Vector(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)


class Letter(object):
	def __init__(self, ascii='a'):
		self.letter = ascii
		if type(ascii) == int:
			self.letter = chr(ascii)
		side = random.choice([-1, 1])
		ratio = min(window.width / 640, window.height / 480)
		self.position = Vector(window.width * (1 - (side + 1) / 2), 0)
		self.velocity = Vector(random.randint(25 * ratio, 75 * ratio) * side, random.randint(35 * ratio, 80 * ratio))
		self.rotation = random.randint(0, 360)
		self.angularVelocity = random.randint(15, 45) * random.choice([-1, 1])
		self.scale = random.randint(max(12 * ratio, 12), max(68 * ratio, 68))
		self.growth = random.randint(-ratio, ratio)
		self.color = [random.randint(0 if useColors else 255, 255), random.randint(0 if useColors else 255, 255), random.randint(0 if useColors else 255, 255), 255]
		self.fade = random.randint(0, 5)
		self.label = pyglet.text.Label(
			ascii, font_name="Source Code Pro", font_size=self.scale, x=self.position.x, y=self.position.y, anchor_x="center", anchor_y="center"
		)
		if useParticles and particleCount:
			for i in range(particleCount):
				particles.add_particles(window, -side)

	def update(self):
		self.position += self.velocity
		self.velocity.y -= 9.81
		self.rotation += self.angularVelocity
		self.angularVelocity *= .99
		self.scale += self.growth
		if self.scale < 12:
			self.scale = 12
		self.growth *= .99
		self.color[3] -= self.fade
		if self.color[3] < 16:
			self.color[3] = 16
		if flickerColors and useColors:
			self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.color[3]]
		self.label.x = self.position.x
		self.label.y = self.position.y
		self.label.font_size = self.scale
		self.label.color = self.color
		if self.position.y < 0:
			del letters[letters.index(self)]

	def blit(self):
		self.label.draw()


def update(dt):
	global keyDelay, globalKeyDelay
	if not keyDelay:
		keyDelay = sum(keys.values()) + globalKeyDelay
		if space:
			letters.append(Letter(chr(random.randint(97, 122))))
		for key in keys:
			if keys[key]:
				letters.append(Letter(key))
	else:
		keyDelay -= 1
	for letter in letters:
		letter.update()
	particles.update_particles(dt)


@window.event
def on_key_press(symbol, modifiers):
	global space, showHelp, useColors, flickerColors, useParticles
	if modifiers == 64 or modifiers == 2:
		showHelp = True
		number = symbol - 48
		change = None
		if number == 1:
			useColors = not useColors
			change = useColors
		elif number == 2:
			flickerColors = not flickerColors
			change = flickerColors
		elif number == 3:
			useParticles = not useParticles
			change = useParticles
		if 0 < number <= len(messages):
			message.text = messages[number - 1] + " to " + str(change)
			message.color = (message.color[0], message.color[1], message.color[2], 255)
			message.x = window.width // 2
			message.y = 3 * window.height // 4
	elif symbol == 32:
		space = not space
	elif symbol < 256:
		keys[chr(symbol)] = True


@window.event
def on_key_release(symbol, modifiers):
	global showHelp
	if symbol == 65517 or symbol == 65507:
		showHelp = False
	if symbol < 256:
		keys[chr(symbol)] = False


@window.event
def on_draw():
	window.clear()
	help.y = window.height - 24
	if showHelp:
		help.draw()
	message.color = (message.color[0], message.color[1], message.color[2], max(message.color[3] - 5, 0))
	message.draw()
	particles.batch.draw()
	for letter in letters:
		letter.blit()

pyglet.clock.schedule_interval(update, 1.0 / 60.0)

pyglet.app.run()
