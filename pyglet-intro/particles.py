import random
import sys

from pyglet.gl import *
from pyglet import graphics


MAX_PARTICLES = 2000
if len(sys.argv) > 1:
    MAX_PARTICLES = int(sys.argv[1])
MAX_ADD_PARTICLES = 100
GRAVITY = -100


def add_particles(window, side):
    particle = batch.add(1, GL_POINTS, None,
                         ('v2f/stream', [window.width / 2 + (window.width / 2 * side), 0]))
    particle.dx = -random.random() * window.width * side / 2
    particle.dy = min(window.height * (.5 + random.random() * .2), 480)
    particle.dead = False
    particles.append(particle)


def update_particles(dt):
    global particles
    constant = 7
    for particle in particles:
        particle.dy += GRAVITY * dt * constant
        vertices = particle.vertices
        vertices[0] += particle.dx * dt * constant
        vertices[1] += particle.dy * dt * constant
        if vertices[1] <= 0:
            particle.delete()
            particle.dead = True
    particles = [p for p in particles if not p.dead]


def loop(dt, window):
    update_particles(dt)

batch = graphics.Batch()
particles = list()
