import pyglet, random

window = pyglet.window.Window(resizable=True)
letters = []


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
		self.opacity = 255
		self.fade = random.randint(0, 5)
		self.label = pyglet.text.Label(
			ascii, font_name="Source Code Pro", font_size=self.scale, x=self.position.x, y=self.position.y, anchor_x="center", anchor_y="center"
		)

	def update(self):
		self.position += self.velocity
		self.velocity.y -= 9.81
		self.rotation += self.angularVelocity
		self.angularVelocity *= .99
		self.scale += self.growth
		if self.scale < 12:
			self.scale = 12
		self.growth *= .99
		self.opacity -= self.fade
		if self.opacity < 16:
			self.opacity = 16
		self.label.x = self.position.x
		self.label.y = self.position.y
		self.label.font_size = self.scale
		self.label.color = (255, 255, 255, self.opacity)
		if self.position.y < 0:
			del letters[letters.index(self)]

	def blit(self):
		self.label.draw()

def update(value):
	for letter in letters:
		letter.update()


@window.event
def on_key_press(symbol, modifiers):
	if modifiers <= 1:
		letters.append(Letter(chr(symbol)))


@window.event
def on_draw():
	window.clear()
	for letter in letters:
		letter.blit()

pyglet.clock.schedule_interval(update, 1.0 / 60.0)

pyglet.app.run()
