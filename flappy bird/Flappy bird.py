from ursina import *

app = Ursina()
Sky()

camera.orthographic = True
camera.fov = 20

bird = Animation("img",
                 collider="box",
                 scale=(2,2,2)
                 )
pipes = []

pipe = Entity(model="quad",
              color=color.green,
              position=(20, 10),
              scale=(3, 15, 1),
              collider="box"
              )


def update():
    bird.y = bird.y - 4*time.dt
    for pipe in pipes:
        pipe.x = pipe.x - 2 *time.dt
    touch = bird.intersects()

    if touch.hit or bird.y < -10:
        quit()



def input(key):
    if key == "escape":
        quit()

    if key == "space":
        bird.y += 2

def newPipe():
    y = random.randint(4, 12)
    up = duplicate(pipe, y=y)
    down = duplicate(pipe, y=y-22)
    pipes.extend((up, down))
    invoke(newPipe, delay=5)


newPipe()


app.run()
