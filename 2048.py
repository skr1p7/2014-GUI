import tkinter as tk
from random import randrange

colors = [
        {"value": 2, "color": "DarkOrange1"},
        {"value": 4, "color": "khaki2"},
        {"value": 8, "color": "khaki3"},
        {"value": 16, "color": "gray"},
        {"value": 32, "color": "chocolate1"},
        {"value": 64, "color": "cornsilk2"},
        {"value": 128, "color": "tomato3"},
        {"value": 256, "color": "goldenrod3"},
        {"value": 512, "color": "gold2"},
        {"value": 1024, "color": "tan1"},
        {"value": 2048, "color": "coral1"},
        ]


def colorPick(value):
    for x in colors:
        if value == x["value"]:
            return x["color"]
    return "ivory2"


root = tk.Tk()
root.title("2048")
root.resizable(0, 0)


class Tile:
    def __init__(self, value=0):
        self.isEmpty = value == 0
        self.value = value
        self.color = "dim gray" if value == 0 else colorPick(value)


class Field:
    def __init__(self, x, y, row, column):
        self.x = x
        self.y = y
        self.end_x = x + 100
        self.end_y = y + 100
        self.row = row
        self.column = column
        self.tile = Tile()


class Game:
    def __init__(self):
        self.fields = []
        self.canvas = tk.Canvas(root, bg="black", width=630, height=650)
        self.move_done = False

    def init(self, win=False):
        self.canvas.pack()
        self.fields = []
        for i in range(0, 4):
            for j in range(0, 4):
                self.fields.append(Field(100+i*110, 200+j*110, i, j))
        self.newTile()
        self.newTile()
        self.draw()

    def draw(self):
        self.canvas.create_rectangle(90, 190, 540, 640,
                                     fill="dark slate gray",
                                     outline="dark slate gray")
        for f in self.fields:
            self.canvas.create_rectangle(f.x, f.y, f.end_x, f.end_y,
                                         fill=f.tile.color,
                                         outline=f.tile.color)
            if f.tile.value > 0:
                font_color = "black" if f.tile.value < 5 else "snow"
                self.canvas.create_text(f.x + 50, f.y + 50,
                                        text=str(f.tile.value),
                                        fill=font_color)

    def newTile(self):
        index = randrange(16)
        value = randrange(2, 5, 2)
        if self.fields[index].tile.isEmpty:
            self.fields[index].tile = Tile(value=value)
        else:
            self.newTile()

    def winner(self):
        for f in self.fields:
            if f.tile.value == 2048:
                root.quit()
                print("You win!")

    def mvRight(self, index, before):
        if index in range(0, 12):
            if self.fields[index].tile.isEmpty:
                self.mvRight(index+4, False)
            else:
                if self.fields[index+4].tile.isEmpty:
                    self.fields[index+4].tile = self.fields[index].tile
                    self.fields[index].tile = Tile()
                    self.move_done = True
                    new_idx = index-4 if before else index+4
                    self.mvRight(new_idx, False)
                else:
                    if self.fields[index].tile.value == self.fields[index+4].tile.value:
                        new_val = self.fields[index].tile.value + self.fields[index+4].tile.value
                        self.fields[index+4].tile = Tile(value=new_val)
                        self.fields[index].tile = Tile()
                        self.move_done = True
                        new_idx = index-4 if before else index+4
                        self.mvRight(new_idx, False)
                    else:
                        self.mvRight(index+4, True)

    def mvLeft(self, index, before):
        if index in range(4, 16):
            if self.fields[index].tile.isEmpty:
                self.mvLeft(index-4, False)
            else:
                if self.fields[index-4].tile.isEmpty:
                    self.fields[index-4].tile = self.fields[index].tile
                    self.fields[index].tile = Tile()
                    self.move_done = True
                    new_idx = index+4 if before else index-4
                    self.mvLeft(new_idx, False)
                else:
                    if self.fields[index].tile.value == self.fields[index-4].tile.value:
                        new_val = self.fields[index].tile.value + self.fields[index-4].tile.value
                        self.fields[index-4].tile = Tile(value=new_val)
                        self.fields[index].tile = Tile()
                        self.move_done = True
                        new_idx = index+4 if before else index-4
                        self.mvLeft(new_idx, False)
                    else:
                        self.mvLeft(index-4, True)



    def mvDown(self, index, before):
        if index in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]:
            if self.fields[index].tile.isEmpty:
                self.mvDown(index+1, False)
            else:
                if self.fields[index+1].tile.isEmpty:
                    self.fields[index+1].tile = self.fields[index].tile
                    self.fields[index].tile = Tile()
                    self.move_done = True
                    new_idx = index-1 if before else index+1
                    self.mvDown(new_idx, False)
                else:
                    if self.fields[index].tile.value == self.fields[index+1].tile.value:
                        new_val = self.fields[index].tile.value + self.fields[index+1].tile.value
                        self.fields[index+1].tile = Tile(value=new_val)
                        self.fields[index].tile = Tile()
                        self.move_done = True
                        new_idx = index-1 if before else index+1
                        self.mvDown(new_idx, False)
                    else:
                        self.mvDown(index+1, True)

    def mvUp(self, index, before):
        if index in [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15]:
            if self.fields[index].tile.isEmpty:
                self.mvUp(index-1, False)
            else:
                if self.fields[index-1].tile.isEmpty:
                    self.fields[index-1].tile = self.fields[index].tile
                    self.fields[index].tile = Tile()
                    self.move_done = True
                    new_idx = index+1 if before else index-1
                    self.mvUp(new_idx, False)
                else:
                    if self.fields[index].tile.value == self.fields[index-1].tile.value:
                        new_val = self.fields[index].tile.value + self.fields[index-1].tile.value
                        self.fields[index-1].tile = Tile(value=new_val)
                        self.fields[index].tile = Tile()
                        self.move_done = True
                        new_idx = index+1 if before else index-1
                        self.mvUp(new_idx, False)
                    else:
                        self.mvUp(index-1, True)

    def mvcRight(self):
        self.mvRight(0, False)
        self.mvRight(1, False)
        self.mvRight(2, False)
        self.mvRight(3, False)
        if self.move_done:
            self.newTile()
            self.move_done = False
        self.draw()

    def mvcLeft(self):
        self.mvLeft(15, False)
        self.mvLeft(14, False)
        self.mvLeft(13, False)
        self.mvLeft(12, False)
        if self.move_done:
            self.newTile()
            self.move_done = False
        self.draw()

    def mvcUp(self):
        self.mvUp(15, False)
        self.mvUp(11, False)
        self.mvUp(7, False)
        self.mvUp(3, False)
        if self.move_done:
            self.newTile()
            self.move_done = False
        self.draw()

    def mvcDown(self):
        self.mvDown(0, False)
        self.mvDown(4, False)
        self.mvDown(8, False)
        self.mvDown(12, False)
        if self.move_done:
            self.newTile()
            self.move_done = False
        self.draw()


game = Game()
game.init()


def eventHandler(event):
    # LEFT
    if event.keycode == 113 or event.keycode == 43:
        game.mvcLeft()
    # DOWN
    elif event.keycode == 116 or event.keycode == 44:
        game.mvcDown()
    # UP
    elif event.keycode == 111 or event.keycode == 45:
        game.mvcUp()
    # RIGHT
    elif event.keycode == 114 or event.keycode == 46:
        game.mvcRight()


root.bind("<Key>", eventHandler)

root.mainloop()