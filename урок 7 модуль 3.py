# a = 5
# b = 1
# c = a + b
# w = "hello" + "world"

# print(type(w)) 

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int):
#             return self.price + other

# item1 = Item("Видиокарта", 20000)
# item2 = Item("Процессор", 10000)
# item3 = Item("Девственность Алины", 10)

# print(item3 + 5)



from tkinter import *
import random
window = Tk()
window.geometry("600x600")

class Fire:
    image = PhotoImage(file="ogon.jpg") 

class Water:
    image = PhotoImage(file="voda.jpg") 

class Earth:
    image = PhotoImage(file="zemla.jpg") 

class Wind:
    image = PhotoImage(file="veter.jpg") 


elements = [Fire(), Earth(), Water(), Wind()]

canvas = Canvas(window, width=600, height=600)
canvas.pack()

for elem in elements:
    img = canvas.create_image(random.randint(50, 550),random.randint(50, 550), image=elem.image)





window.mainloop()