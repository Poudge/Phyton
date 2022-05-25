from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

app = Ursina()
Sky(texture='sky_sunset')

ground = Entity(
    model='plane',
    collider='mesh',
    scale=(100, 1, 100),
    color=color.olive,
    texture='1'
)

player = FirstPersonController(collider='box')
player.speed = 5
player.jump_height = 3


window.fullscreen = True
blocks = []
directions = []

for n in range(100):
    randomNumber = uniform(-2, 2)
    block = Entity(
        model='cube',
        texture='white_cube',
        color=color.random_color(),
        scale=(2, 1, 2),
        collider='box',
        position=(randomNumber, n + 1, 3 * n + 5)
    )
    blocks.append(block)
    if randomNumber < 0:
        directions.append(1)
    else:
        directions.append(-1)


# update(), input()

def input(key):
    if key == 'escape':
        quit()


def update():
    i = 0
    for b in blocks:
        b.x -= directions[i] * time.dt
        if abs(b.x) > 5:
            directions[i] *= -1
        if b.intersects().hit:
            player.x -= directions[i] * time.dt
        i += 1



app.run()
