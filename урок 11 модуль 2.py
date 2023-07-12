# *** Полиморфизм ***
 
# Статическая типизация

# int a = 5

# Динамическая типизация

# a = 5
# a = "hello"
# a = True


# def func(a):
#     print(a)

# func(True)


# class Animal:
#     legs = 4
#     tail = 1
#     def voice(self):
#         print("какой-то звук")

# class Cat(Animal):
#     def voice(self):
#         print("мяу-мяу")

# class Dog(Animal):
#     def voice(self):
#         print("гав-гав")

# animal = Animal()
# cat = Cat()
# dog = Dog()

# farm_band = [animal, cat, dog]

# for animal in farm_band:
#     if isinstance(animal, Cat):
#         animal.voice()
#     elif isinstance(animal, Dog):
#         animal.voice()
#     else:
#         animal.voice()



# class Animal:
#     _legs = 4
#     __tail = 1
#     def voice(self):
#         print("какой-то звук")
    
#     def getter(self):
#         print(self.__tail)

# animal = Animal()
# animal._legs = 1
# print(animal._Animal__tail)


#Декораторы

# def func_decorator(func):
#     def inner():
#         print("Супер базовый и важный функционал, к которому y нас нет доступа")
#         func()
#         print("...end")
#     return inner

# @func_decorator
# def some_func():
#     print("что-то добавили")

# some_func()
 


import tkinter as tk
import requests
from bs4 import BeautifulSoup
import random


def draw_menu():
    all_widgets = win.place_slaves()
    for i in all_widgets:
        i.destroy()
    label_title = tk.Label(win, text="Что вы хотите сделать?", font=("arial", 24), fg="white", bg="orange")
    label_title.place(width=700, height=50)

    btn1 = tk.Button(win, text="Узнать факт", font=("arial", 18), fg="black", bg="#D6D6D6", command=get_interesting_fact)
    btn1.place(x=25, y=75, width=300)
    btn2 = tk.Button(win, text="Посмотреть на котиков", font=("arial", 18), fg="black", bg="#D6D6D6", command=get_cat)
    btn2.place(x=375, y=75, width=300)


def clear():
    all_widgets = win.place_slaves()
    for i in all_widgets:
        i.destroy()
    home_button()


def home_button():
    home_btn = tk.Button(win, text="Домой", font=("arial", 24), command=draw_menu)
    home_btn.place(x=25, y=500, width=150)


def get_cat():
    clear()
    response = requests.get("https://fonwall.ru/search?q=кошки")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    allcats = html.find_all("figure", class_="b-popup bubble-node b-bubble-ui b-popup-noclosecontrol") 
    cats = []
    for i in allcats:
        cats.append(i.find("img").get("src"))
    print(cats)

def get_interesting_fact():
    response = requests.get("https://dymontiger.livejournal.com/15806868.html")
    response = response.content
    html = BeautifulSoup(response, "lxml")
    fact = html.find(class_='entry-content').text
    print(fact)


    

win = tk.Tk()
win.geometry("700x600")
draw_menu()


win.mainloop() 