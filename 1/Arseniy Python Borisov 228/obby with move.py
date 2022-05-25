import timeit

from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController

import random

app = Ursina()
window.fullscreen = True

ground = Entity(
    model='plane',
    texture='grass',
    color=color.olive,
    collider='mesh',
    scale=(10, 1, 10)
)

player = FirstPersonController(collider='box')
Sky(texture='sky_sunset')
player.speed = 10
player.jump_height = 2
player.gravity = 2

blocks = []
directions = []

for i in range(150):
    randomNumber = random.uniform(-2, 2)
    block = Entity(
        model='cube',
        texture='white_cube',
        color=color.random_color(),
        scale=(3, 0.5, 3),
        collider='box',
        position=(randomNumber, 1+i, 3*i+3)
    )
    blocks.append(block)
    if randomNumber < 0:
        directions.append(1)
    else:
        directions.append(-1)

def input(key):
    if key == 'escape':
        quit()

def update():
    i = 0
    for block in blocks:
        block.x -= directions[i] * time.dt
        if abs(block.x) > 5:
            directions[i] *= -1
        if block.intersects().hit:
            player.x -= directions[i] * time.dt

        i += 1



app.run()
