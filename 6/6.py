from ursina import *

app = Ursina()
camera.orthographic = True
camera.fov = 4
camera.position = (1, 1)

player = Entity(name='O', color=color.azure)
cursor = Tooltip(
    color=player.color,
    origin=(0, 0),
    scale=4,
    enabled=True
)
cursor.background.color = color.clear

bg = Entity(
    model='quad',
    parent=scene,
    scale=(16, 8),
    color=color.black33,
    z=10
)

board = [[None for x in range(3)] for y in range(3) ]

for x in range(3):
    for y in range(3):
        b = Button(
            parent=scene,
            position=(x, y),
            color=color.light_gray
        )
        board[x][y] = b

        def on_click(button=b):
            button.text = player.name
            button.color = player.color
            button.collision = False
            victory()

            if player.name == 'O':
                player.name = 'X'
                player.color = color.orange
            else:
                player.name = 'O'
                player.color = color.azure
            cursor.text = ''
            cursor.color = player.color

        b.on_click = on_click


def victory():
    name = player.name

    win = (
        (board[0][0].text == name and board[0][1].text == name and board[0][2].text == name)
        or
        (board[1][0].text == name and board[1][1].text == name and board[1][2].text == name)
        or
        (board[2][0].text == name and board[2][1].text == name and board[2][2].text == name)
        or
        (board[0][0].text == name and board[1][0].text == name and board[2][0].text == name)
        or
        (board[1][0].text == name and board[1][1].text == name and board[2][1].text == name)
        or
        (board[0][2].text == name and board[1][2].text == name and board[2][2].text == name)
        or
        (board[0][0].text == name and board[1][1].text == name and board[2][2].text == name)
        or
        (board[0][2].text == name and board[1][1].text == name and board[2][0].text == name)

    )

    if win:
        destroy(cursor)
        Panel(z=1, scale = 10, model='quad')
        t = Text(f'Игрок\n{name}\nПобедил', scale = 3, background=True, origion=(0, 0))
        t.create_background(padding=(0.5, 0.25))
        t.background.color = player.color




app.run()
