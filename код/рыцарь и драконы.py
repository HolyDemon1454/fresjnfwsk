from tkinter import *
import random
window = Tk()
w = 600
h = 600
window.geometry(str(w) + "x" + str(h))
canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)
bg_photo = PhotoImage(file="bg_2.png")
canvas.create_image(300, 300, image=bg_photo)

class Knight:
    def __unit__(self):
        self.x = 70
        self.y = h // 2
        self.v = 0
        self.v_x = 0
        self.photo = PhotoImage(file="knight.png")

    def up(self, event):
        self.v = -5
    def down(self, event):
        self.v = 5
    def right(self, event):
        self.v_x = +3
    def left(self, event):
        self.v_x = -3

    def stop(self, event):
        self.v = 0
        self.v_x = 0


class Dragon:
    def __unit__(self):
        self.x = 750
        self.y = random.randint(100, 500)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file="dragon.png")


knight = Knight()
dragons = []
for i in range(3):
    dragons.append(Dragon())  


def game():
    canvas.delete("all")
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    if knight.y <= 52:
        knight.y = 53
    if knight.y >= 544:
        knight.y = 543
    if knight.x <= 50:
        knight.x = 51
    if knight.x >= 550:
        knight.x = 551

    knight.y += knight.v

    for dragon in dragons:
        dragon.x -= dragon.y  
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

    window.after(5, game) 

game()

window.bind("<Key-Up>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind("<KeyRelease>", knight.stop)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)
window.mainloop() 
