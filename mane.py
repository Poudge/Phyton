from ursina import *


class Game(Ursina):
    def __init__(self):
        super.__init__()
        window.color = color.black
        window.fullscreen = True
        AmbientLight(color=(0.5, 0.5, 0.5, 1))
        DirectionalLight(color.=(0.5, 0.5, 0.5, 1))
        self.MAP_SIZE = 20
        camera.position = (10,-20.5, -20)
        camera.rotation_z = -57

    def creat_map(self):
        pass

    def new_game(self):
        pass

    def input(self):
        pass

    def chek_apple_eat(self):
        pass

    def chek_game_over(self):
        pass

    def update(self):
        pass


