import pyglet

window = pyglet.window.Window()
image = pyglet.image.load("ace_of_spades.png")
sprite = pyglet.sprite.Sprite(image)

card.sprite = pyglet.sprite.Sprite(pyglet.image.load(card.name + "_of_" + card.suit + ".png"))


@window.event
def on_draw():
	window.clear()
	sprite.scale = (window.height / sprite.height)
	sprite.draw()

pyglet.app.run()
