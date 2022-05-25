from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
Sky(texture="5")

player = FirstPersonController()
window.fullscreen = True

boxes = []

for i in range(50):
    for k in range(50):
        box = Button(
            position=(i, 0, k),
            color=color.white,
            highlight_color=color.white66,
            model='cube',
            parent=scene,
            texture=load_texture("1")
        )
        boxes.append(box)

def input(key):
    if key == "escape":
        quit()

    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)
            if key == "right mouse down":
                newBox = Button(
                    position = box.position + mouse.normal,
                    color = color.white,
                    model = "cube",
                    hightlight_color = color.white,
                    parent = scene,
                    texture=load_texture("2")
                )
                boxes.append(newBox)
            if key == "1":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color = color.white,
                    model="cube",
                    parent = scene,
                    texture=load_texture("3")
                )
                boxes.append(newBox)
            if key == "2":
                newBox = Button(
                    position = box.position + mouse.normal,
                    color=color.white,
                    model = "cube",
                    parent = scene,
                    texture=load_texture("4")
                )
                boxes.append(newBox)

            if key == "3":
                newBox = Button(
                    position = box.position + mouse.normal,
                    color=color.white,
                    model = "cube",
                    parent = scene,
                    texture=load_texture("7")
                )
                boxes.append(newBox)

            if key == "4":
                newBox = Button(
                    position = box.position + mouse.normal,
                    color=color.white,
                    model = "cube",
                    parent = scene,
                    texture=load_texture("6")
                )
                boxes.append(newBox)

            if key == "5":
                newBox = Button(
                    position = box.position + mouse.normal,
                    color=color.white,
                    model = "cube",
                    parent = scene,
                    texture=load_texture("8")
                )
                boxes.append(newBox)

            if key == "6":
                newBox = Button(
                    position = box.position + mouse.normal,
                    color=color.white,
                    model = "cube",
                    parent = scene,
                    texture=load_texture("9")
                )
                boxes.append(newBox)

                if key == "7":
                    newBox = Button(
                    position = box.position + mouse.normal,
                    color=color.white,
                    model = "cube",
                    parent = scene,
                    texture=load_texture("10")
                    )
                boxes.append(newBox)

app.run()

