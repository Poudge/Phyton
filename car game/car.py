import timeit

from ursina import *
import random

game = Ursina()
camera.orthographic = True
camera.fov = 10

car = Entity(model='quad',
             texture='img/car.png',
             collider='box',
             scale=(2,1),
             rotation_z=-90,
             y=0
             )
road1 = Entity(model='quad',
               texture='img/road.png',
               scale=15,
               z=1)
road2 = duplicate(road1,
                  y=15)
roads = [road1, road2]

enemy = []

def input(key):
    if key == 'escape':
        quit()

def spawnCars():
    n = random.uniform(-2, 2)
    newCar = duplicate(car,
                       texture='img/enemy.png',
                       x=2*n,
                       y=25,
                       color=color.random_color(),
                       rotation_z = 90 if n < 0 else -90
                       )
    enemy.append(newCar)
    invoke(spawnCars, delay=0.5)
spawnCars()

def update():
    if held_keys['a']:
        car.x -= 5 * time.dt
    if held_keys['d']:
        car.x += 5 * time.dt

    for road in roads:
        road.y -= 6 * time.dt
        if road.y < -15:
            road.y += 30

    for c in enemy:
        if c.x < 0:
            c.y -= 10 * time.dt
        else:
            c.y -= 5 * time.dt
        if c.y < -10:
            enemy.remove(c)
            destroy(c)
        if car.intersects().hit:
            car.shake()

game.run()
