from ursina import *
import random as r

app = Ursina()
Sky()

camera.orthographic = True
camera.fov = 20

bird = Animation("img",
                 collider="box",
                 scale=(2, 2, 2),
                 x=-8
                 )

def input(key):
    if key == "escape":
        quit()

    if key == "space":
        bird.y += 2


def update():
    bird.y -= 3 * time.dt

    for p in pipes:
        p.x -= 3 * time.dt

    touch = bird.intersects()
    if touch.hit or bird.y < - 10:
        quit()


pipes = []

pipe = Entity(model="quad",
              color=color.green,
              texture="white_cube",
              position=(20, 20),
              scale=(3, 15, 1),
              collider="box"
              )


def newPipe():
    y = r.randint(4, 12)
    up = duplicate(pipe, y=y)
    down = duplicate(pipe, y=y - 22)
    pipes.extend((up, down))
    invoke(newPipe, delay=5)


newPipe()

app.run()
