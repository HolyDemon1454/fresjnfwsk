#n = [] 
#print("введите") 
#for i in range(6):
#   income =int(input("введите свою зп: ")) 
#    n.append(income * 0.3)
#print(n)
#print("ваши накопления составят", sum(n)) 


#import random 
#a = ["кот ", "собака ", "попугай "]
#b = ["большой ", "пушистый", "умный"] 
#print(random.choice(a) + random.choice(b)) 
#print(random.choice(a) + random.choice(b)) 
#print(random.choice(a) + random.choice(b))


#from random import randint
#a = [randint(0, 5) for _ in range(30)]
#print(a)
#print(a.count(5))






#temp_list = [] 
#for i in range(7):
#   temp =int(input("введите кол во градусов на улице: ")) 
#   temp_list.append(temp)
#print(temp)
#print(sum(temp_list)/len(temp_list))


#favorite_number = "5" 
#number = input("введите кол во градусов: ")
#if number == favorite_number:
#    print("прохладно")
#else:
#    print("пофиг")




#favorite_number = "5" 
#another_number = "4"
#another_numberr = "3"
#another_numberrr = "6"
#another_numberrrr = "7"
#another_numberrrrr = "8"
#number = input("введите кол во градусов: ")
#if number == favorite_number:
#    print("прохладно")
#elif number == another_number:
#    print("холодно")
#elif number == another_numberr:
#    print("очень холодно")
#elif number == another_numberrr:
#    print("тепло")
#elif number == another_numberrrr:
#    print("жарко")
#elif number == another_numberrrrr:
#    print("очень жарко")
#else:
#    print("мне пофиг")




# from random import randint
# a = 1
# print('Игра "Орел-Решка"')
# while (a<2) and (a>0):
#     a = int(input('Загадай орла или решку (1 или 2) :'))
#     print(['Выиграл!','Проиграл'][a==randint(1,2)])


# def get_input_parameters():
#     list_nums = []
#     for i in range(int(input('Количество цифр в списке: '))):
#         list_nums.append(int(input(f'Введите {i+1} число: ')))
#     return list_nums
 
 
# def sort_list(original_list):
#     for i in range(len(original_list)):
#         for cur_elem in range(i, len(original_list)):
#             if original_list[i] > original_list[cur_elem]:
#                 original_list[cur_elem], original_list[i] = original_list[i], original_list[cur_elem]
#     return original_list
 
# def display_result(lst):
#     print('Оригинальный список:')
#     print(lst)
#     print('Отсортированный список:')
#     print(sort_list(lst))
 
 
# display_result(get_input_parameters())



# import random
# number = random.randint(1,10)
# numberr = int(input("угадай число"))
# difference = numberr - number
# if numberr == number:
#     print("мощьный")
# elif difference == 1 or difference == -1:
#     print("почти")
# else:
#     print("анскилл")



# a = {
#      "молоко": 65,
#      "кефир": 70,
#      "список": [12, 242, 231, 5],
#      "словарь": {
#         "ключ": "значение"
#      }
#  }  

# print(a.get("чипсы"))



# engl = {
#     "яблоко": "apple",
#     "кот": "cat",
#     "молоко": "milk"
# }
# word = input("на русском введи ")
# if word in engl:
#     print(word+ "на английском будет: " +engl[word])
# else:
#     print("пошёл нафиг")

# films = {
#     "начало": "леонардо",
#     "человек паук": "том",
#     "терминатор": "арнольд",
#     "драйв": "лох"
# }

# actor = "лох"
# film = input("введите фильм который хотите: ") 
# if film in films:
#     actor = "лох"
#     if actor == films[film]:
#         print("да")
#     else:
#         print("нет")





# minecraft = [
#     {
#         "q": "сколько блоков в игре?",
#         "qq": ["200", "300", "400", "много"],
#         "qqq": 4
#  },
#     {"q": "какой вес может носить игрок в инвенторе в выживании без использования читов и модов?",
#     "qq": ["60кг", "900кг", "6000000кг+", "4000000кг+"],
#     "qqq": 3

#     },
#     {"q": "какой моб победил на голосовании майнкон в 2022?",
#         "qq": ["нюхач", "туфовый голем", "негодяй", "его ещё не было"],
#         "qqq": 1

#     },

# ]

# score = 0
# for q in minecraft:
#     print(q["q"])
#     qqqq = 0
#     for qq in q["qq"]:
#         qqqq = qqqq + 1
#         print(qqqq, " ", qq)
#     qqqq = int(input("введите ответ: "))
#     if qqqq == q["qqq"]:
#         print("верно +1 очко")
#         score += 1
#     else:
#         print("Неверно анскилл 0 очков")
# print(f"Ваши очки: {score}")


# violator_songs = {
#     "astral step": 1.70
# }
# {
#     "666": 1.05
# }
# {
#     "showdawn": 2.04
# }
# {
#     "death note": 1.37
# }
# {
#     "1000-7": 2.14
# }

# count = int(input('Сколько песен выбрать? '))
# all_time = 0.0
 
# for i in range(count):
#     query = f'Название {i + 1} песни: '
#     song_name = input(query)
#     all_time += violator_songs.get(song_name, 0)
 
# print(f'Общее время звучания песен: {round(all_time, 2)} минут')




# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
 
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
 
# for product_name, product_code in goods.items():
#     item_total_quantity = 0
#     item_total_cost = 0
#     for product in store[product_code]:
#         item_quantity = product['quantity']
#         item_cost = product['price']
#         item_total_cost += item_quantity * item_cost
#         item_total_quantity += item_quantity
#     print('{0} - {1} шт, общая стоимость {2} рублей'.format(product_name, item_total_quantity, item_total_cost))


# file = open("result.txt" ,"w")
# file.write("i goule")

# file = open("result.txt" ,"r")
# s = file.read()
# print(s) 

# file = open("result.txt" ,"r")
# a = []
# for line in file.readlines():
#     print(line)


# name = input("введите имя: ")
# minecraft = [
#     {
#         "q": "сколько блоков в игре?",
#         "qq": ["200", "300", "400", "много"],
#         "qqq": 4
#  },
#     {"q": "какой вес может носить игрок в инвенторе в выживании без использования читов и модов?",
#     "qq": ["60кг", "900кг", "6000000кг+", "4000000кг+"],
#     "qqq": 3

#     },
#     {"q": "какой моб победил на голосовании майнкон в 2022?",
#         "qq": ["нюхач", "туфовый голем", "негодяй", "его ещё не было"],
#         "qqq": 1

#     },

# ]

# score = 0
# for q in minecraft:
#     print(q["q"])
#     qqqq = 0
#     for qq in q["qq"]:
#         qqqq = qqqq + 1
#         print(qqqq, " ", qq)
#     qqqq = int(input("введите ответ: "))
#     if qqqq == q["qqq"]:
#         print("верно +1 очко")
#         score += 1
#     else:
#         print("Неверно анскилл 0 очков")
# print(f"Ваши очки: {score}")
# file = open("result.txt", "a")
# file.write(name + ": " + str(score) + "\n")
# file.close()

# filer = open("result.txt", "r")
# print(filer.read())


# функция
# def summ(a):
#     s = a + 5
#     return s
# result = summ(4)
# print(result)

# def cal(a, b, operand):
#     if operand == "+":
#         result = a + b
#     elif operand == "-":
#         result = a - b
#     elif operand == "/":
#         result = a / b
#     elif operand == "*":
#         result = a * b
#     return result
# a = int(input("Введите 1 число: ")) 
# b = int(input("Введите 2 число: ")) 
# op = input("Введите операцию: ")
# print(cal(a, b, op))
# file = open("result.txt", "a")
# file.write(str(cal(a, b, op)) + "\n") 
# file.close()

# filer = open("result.txt", "r")
# print(filer.read())



# n = int(input('Введите N:'))
# def summa_n(n):
#     if n==0:
#         return n
#     else:
#         return(n+summa_n(n-1))
# print(f'Сумма чисел от 1 до {n} = {summa_n(n)}')


# def greeting():
#     for i in range(5):
#         a = input('Зайдёте? Да/Нет: ')
#         if a == 'Да':
#             print('Привет!')
#             print('Добро пожаловать!')
#         print('Следующий.\n')
 
 
# greeting()




# from tkinter import *
# window = Tk()
# window.geometry("700x500") 
# window.title("goule") 

# facts = [
#     {"text": "алмаз спавнится на 12 высоте", "right":1}
# ]
# cur_q=0
# points=0
# def check():
#     global cur_q,points
#     answer = var.get()
#     if bool(answer) == facts[cur_q]['right']:
#         points+=1
#     if cur_q < len(facts)-1:
#         cur_q+=1
#         fact['text'] = facts[cur_q]['text']
#     else: 
#         points_label = Label (text='Вы набрали ' + str(points) + ' очка',
#                         font=('Arial',34),fg='red',bg='white')
#         points_label.place(x=0,y=0,width=700,height=250)

# label_title = Label(text = 'Тестирование на майнкрафтера',font=('Arial',24),fg='black',bg='white')
# label_title.place(width=700, height=50, x=0, y=0)

# fact = Message(text = facts[cur_q]['text'], font=('Arial',14),
#         width=680,borderwidth=0)
# fact.place(x=10,y=70)

# var = IntVar()
# true = Radiobutton(text = 'Верно',variable = var ,value=1)
# true.place(x=10,y=120)

# false = Radiobutton(text = 'Ложь',variable = var, value=0)
# false.place(x=10,y=170)

# b=Button(text='Ответить', font=('Arial',24),fg='black',command=(check))
# b.place(x=200,y=130)


# window.mainloop()
# if points % 10 == 0:


# from tkinter import *
# import random

# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
# points = 0
# pointss = 0
# def check():
#     global points
#     b.place(x=random.randint(1, 550), y=random.randint(1, 350))
#     points += 1
#     label['text'] = points

# def check():
#     global pointss
#     a.place(x=random.randint(1, 550), y=random.randint(1, 350))
#     pointss += 1
#     labell['text'] = pointss


# a = Button(text='нажми меня', font=('Ariall', 20), fg='black', command=check)
# a.place(x=500, y=100)
# labell = Label(text=pointss, font=('Ariall', 15), fg='black')
# labell.place(x=50, y=10)

# b = Button(text='нажми меняя', font=('Arial', 20), fg='black', command=check)
# b.place(x=150, y=100)
# label = Label(text=points, font=('Arial', 15), fg='black')
# label.place(x=10, y=10)
 
# window.mainloop()



# from tkinter import *
# window = Tk()
# window.geometry("900x300")
# window.resizable(width=False, height=False)
# window.config(bg="black")
# text = Label(text="ваш дом взорвётся через:", bg="black", font=("Courier New", 34), fg="green")
# text.place(x=100,y=100, width=700, height=100 )
# count_text = Label(text="10", fg="green", bg="black", font=("Courier New", 36))

# def count_start():
#     if int(count_text["text"]) > 0:
#         count_text["text"] = int(count_text["text"])-1
#         count_text.place(x=250, y=25, width=400, height=100)
#         window.after(1000, count_start)
#     else:
#         width = window.winfo_screenwidth()
#         height = window.winfo_screenwidth()
#         window.geometry(str(width) + "x" + str(height))
        
#         photo = PhotoImage(file = "ogon_1.jpg")
#         label = Label(image=photo, bg="black")
#         label.image = photo
#         label.place(width=width, height=height, x=0, y=0)

# def on_close():
#     count_start()
   
# window.protocol("WM_DELETE_WINDOW", on_close)


# window.mainloop()



# import requests
# from bs4 import BeautifulSoup 
# import random
# respons = requests.get("https://pikabu.ru/story/100_interesnyikh_faktov_obo_vsem_na_svete_4109303")
# respons = respons.content
# html = BeautifulSoup(respons, "html.parser")
# facts = html.find_all(class_=_"post-title")  
# fact = random.choice(facts) 
# print(fact.text)
# print(facts[0].a.attrs["href"])  

# import requests
# from re import findall
# response = requests.get('http://www.columbia.edu/~fdc/sample.html').text
# result_beta = findall(r'>.+</h3>', response)
# release = list(map(lambda x: x[1:-5], result_beta))
# print(release)

# import requests
# from bs4 import BeautifulSoup
# url = 'https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets'
# soup = BeautifulSoup(requests.get(url).text)
# list_rows = soup.select_one("div.ecomerce-items-ajax")['data-items']
# print(list_rows)

# import requests
# from bs4 import BeautifulSoup
# respons = requests.get("https://store.steampowered.com/")
# respons = respons.content
# html = BeautifulSoup(respons, "html.parser")
# print(respons.text)


# i = 0
# while i<10:
#     print(i)
#     i+=1

# a = 0
# s = 0
# while a != -1:
#     s += a
#     a = int(input())
# print(s)



# import requests
# from bs4 import BeautifulSoup 
# import random
# def get_interesting_concert():
#     respons = requests.get("https://kudagoo.com/msk/concerts/")
#     respons = respons.content
#     html = BeautifulSoup(respons, "html.parser")
#     concert = random.choice(html.find_all(class_="post-title"))
#     print(concert.text)
#     print(concert.a.attrs["href"])
# user_wish = ""
# while user_wish != "-":
#     user_wish = input("Чем бы вы хотели заняться").lover()
#     if user_wish == "концерт":
#         get_interesting_concert()
#     else :
#         print("(((")
    

# from fpdf import FPDF
# pdf = FPDF("P", "cm", (10, 20))
# pdf.add_page()
# pdf.add_font("courier", "", "C:\WINDOWS\FONTS\COUR.ttf", uni=True)
# pdf.set_text_color(0,255,0)
# pdf.set_fill_color(10,134,92)
# pdf.set_draw_color(0, 0, 255)
# pdf.set_font("courier", size=25)
# pdf.cell(8, 3, txt="Скоро новый год", align="C", fill=True, border=1) 
# pdf.image("ogon_1.jpg", h=0, w=10, x=0, y=5)
# pdf.output("test_fpdf.pdf")



# number = int(input('Введите число: '))
# summa = 0
# while number != 0:
#     summa += number
#     number = int(input('Введите следующее число: '))
# print(summa)


# password = int(input('Введите пароль: '))
# while password != 235:
#     print('иди от сюда ! ')
#     password = int(input('Введите пароль правильно: '))
# print('Пароль верный! Добро пожаловать.')

# import xlrd, xlwt
# rb = xlrd.open_workbook('../ArticleScripts/ExcelPython/xl.xls',formatting_info=True)
# sheet = rb.sheet_by_index(0)
# val = sheet.row_values(0)[0]
# vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
# wb = xlwt.Workbook()
# ws = wb.add_sheet('Test')
# ws.write(0, 0, val[0])
# i = 0
# for rec in vals:
#     ws.write(i,1,rec[0])
#     i =+ i
# wb.save('../ArticleScripts/ExcelPython/xl_rec.xls')
# import openpyxl
# wb = openpyxl.load_workbook(filename = '../ArticleScripts/ExcelPython/openpyxl.xlsx')
# sheet = wb['test']
# val = sheet['A1'].value
# vals = [v[0].value for v in sheet.range('A1:A2')]
# sheet['B1'] = val
# i = 0
# for rec in vals:
#     sheet.cell(row=i, column=2).value = rec
#     i =+ 1
# wb.save('../ArticleScripts/ExcelPython/openpyxl.xlsx')

# from datetime import datetime
# from fpdf import FPDF
# pdf = FPDF ("P", "mm", "A4")
# pdf.add_page()
# pdf.image("ogon_1.jpg", h=297, w=210, x=0, y=0)
# pdf.add_font("comic", "", "C:\WINDOWS\FONTS\COMIC.ttf", uni=True)
# pdf.set_font("comic", size=35)
# friend_name = input("введите имя друга: ")
# pdf.cell(0, 95, ln=1)
# pdf.cell(0, 20, txt="Дорогой " + friend_name + "!", align="C", ln=1 )
# pdf.set_font("comic", size=18)
# pdf.set_right_margin(50)
# pdf.set_left_margin(50)
# message = input("Введите поздравление: ")
# pdf.multi_cell(0, 20, message, align="C")
# pdf.set_text_color(124, 90, 147)
# today = datetime.today().strftime("%d.%m.%Y")
# pdf.cell(0, 20, txt=today, align="R", ln=1)
# author_name = input("Ведите ваше имя: ")
# pdf.cell(0, 20, txt=author_name, align="R", ln=1)
# pdf.output("bday_card.pdf") 


# i = 1

# while i <= 10:
#     print(i) 
#     i += 1
# else:
#     print('Цикл окончен, i =', i)


# from tkinter import *

# window = Tk()
# window.geometry('700x600')

# def draw_menu():
#     clear()
#     label_title = Label(text='Что бы вы хотели сделать?', font=('Arial', 24), fg='white', bg='orange')
#     label_title.place(width=700, height=50, x=0, y=0)
#     b_1 = Button(text='Узнать что-то новое', font=('Arial', 18), fg='black', command=clear)
#     b_1.place(x=25, y=75, width=300)

#     b_2 = Button(text='Посмотреть на котиков', font=('Arial', 18), fg='black', command=clear)
#     b_2.place(x=375, y=75, width=300)

# def clear():
#     all_widgets = window.place_slaves()
#     for l in all_widgets:
#         l.destroy()
#         draw_home_button()

# def draw_home_button():
#     b = Button(text='Домой', font=('Arial', 24), fg='black', command=draw_menu)
#     b.place(x=25, y=500, width=150)

# draw_menu()

# window.mainloop()










# import tkinter as tk
# import requests
# from bs4 import BeautifulSoup
# import random


# def draw_menu():
#     all_widgets = win.place_slaves()
#     for i in all_widgets:
#         i.destroy()
#     label_title = tk.Label(win, text="Что вы хотите сделать?", font=("arial", 24), fg="white", bg="orange")
#     label_title.place(width=700, height=50)

#     btn1 = tk.Button(win, text="Узнать факт", font=("arial", 18), fg="black", bg="#D6D6D6", command=get_interesting_fact)
#     btn1.place(x=25, y=75, width=300)
#     btn2 = tk.Button(win, text="Посмотреть на котиков", font=("arial", 18), fg="black", bg="#D6D6D6", command=get_cat)
#     btn2.place(x=375, y=75, width=300)


# def clear():
#     all_widgets = win.place_slaves()
#     for i in all_widgets:
#         i.destroy()
#     home_button()


# def home_button():
#     home_btn = tk.Button(win, text="Домой", font=("arial", 24), command=draw_menu)
#     home_btn.place(x=25, y=500, width=150)


# def get_cat():
#     clear()
#     response = requests.get("https://fonwall.ru/search?q=кошки")
#     response = response.content
#     html = BeautifulSoup(response, "html.parser")
#     allcats = html.find_all("figure", class_="b-popup bubble-node b-bubble-ui b-popup-noclosecontrol") 
#     cats = []
#     for i in allcats:
#         cats.append(i.find("img").get("src"))
#     print(cats)

# def get_interesting_fact():
#     clear()
#     response = requests.get("https://dymontiger.livejournal.com/15806868.html")
#     response = response.content
#     html = BeautifulSoup(response, "html.parser")
#     for el in html.select(".items > .article-summary"):
#         title = el.select(".caption > a")
#     print(title[0].text)
    

# win = tk.Tk()
# win.geometry("700x600")
# draw_menu()


# win.mainloop()


# import tkinter as tk
# import requests

# from io import BytesIO
# from PIL import Image, ImageTk

# url = "https://www6b3.wolframalpha.com/Calculate/MSP/MSP14531gg5c35255f535bi0000683dg2hfh4g5hh7i?MSPStoreType=image/gif&s=6"

# root = tk.Tk()


# def load_image():
#     label.config(text='Loading an image...')
#     root.update()
#     try:
#         response = requests.get(url, timeout=10)
#     except requests.exceptions.Timeout:
#         label.config(text='Timeout error')
#     else:
#         if response.status_code != 200:
#             label.config(text=f'HTTP error {response.status_code}')
#         else:
#             pil_image = Image.open(BytesIO(response.content))
#             image = ImageTk.PhotoImage(pil_image)
#             label.config(image=image, text='')

#             # прикрепляем ссылку на изображение к объекту label,
#             # чтобы изображение не удалил сборщик мусора
#             label.image = image  


# tk.Button(root, text='Load an image', command=load_image).pack()
# label = tk.Label(root)
# label.pack()

# root.mainloop()






# 5923726444:AAFzro1TD8ZMOzD-AwQC4qXUaVtHikPVe_s 

# import telebot
# import random
# token = "5923726444:AAFzro1TD8ZMOzD-AwQC4qXUaVtHikPVe_s"
# bot = telebot.TeleBot(token) 

# @bot.message_handler(commands=["start", "help"])
# def send_wecome(message):
#     welcome = "Привет, я чертила а не бот. Могу ответить, а могу не ответить (/start /help /pcem /cat)"
#     bot.send_message(message.from_user.id, welcome)

# @bot.message_handler(commands=["cat"])
# def send_cat(message):
#     # cat_number = str(random.randint(1,9))
#     # cat_ing = open("ing/" + cat_number + ".jpg", "rb")
#     # bot.send_photo(message.chat.id, cat_ing)
#     cat_ing = open("ogon_1.jpg", "rb")
#     bot.send_photo(message.chat.id, cat_ing)


# @bot.message_handler(commands=["poen"])
# def send_wecome(message):
#     poen = "внимание анекдот: появился как то в зоне чёрный сталкер..................."
#     bot.send_message(message.from_user.id, poen)


# @bot.message_handler(content_types=["text"])
# def get_text_message(message):
#     if message.text == "привет":
#         bot.send_message(message.from_user.id, "Салам")
#     if message.text == "пока":
#         bot.send_message(message.from_user.id, "бб")
#     else:
#          bot.send_message(message.from_user.id, "я не знаю таких слов")



# bot.polling()



# try:
#     num_1 = int(input("введите число 1 "))
#     num_2 = int(input("введите число 2 "))
#     oper = input("введите операцию ")
# except ValueError:
#     print("вы ввели неверное значение")
# else:
#     if oper == "+":
#         print(num_1+num_2)
#     else:
#         print(num_1-num_2) 
# finally:
#     print("гг я ливаю")


# a = ["кухня", "гостинная", "ванная", "спальня"] 
# for i in a:
#     print(i, "в квартире")


# def add(x, y):
#     s = x + y
#     return s
# for i in range(5):
#     num_1 = int(input("введите число 1 "))
#     num_2 = int(input("введите число 2 "))
#     s = add(num_1, num_2)
#     print(s)



# def calculator():
#     print("укажите интересующую вас операцию ")
#     print("*")
#     print("/")
#     print("+")
#     print("-")
#     print("D")
#     operation = input("> ")
#     if operation == "*":
#         try:
#             num_1 = int(input("введите число 1 "))
#             num_2 = int(input("введите число 2 "))
#         except ValueError:
#             print("неизветное значение")
#         else:
#             print(num_1*num_2)
#     if operation == "/":
#         try:
#             num_1 = int(input("введите число 1 "))
#             num_2 = int(input("введите число 2 "))
#         except ValueError:
#             print("неизветное значение")
#         else:
#             print(num_1/num_2)
#     if operation == "+":
#         try:
#             num_1 = int(input("введите число 1 "))
#             num_2 = int(input("введите число 2 "))
#         except ValueError:
#             print("неизветное значение")
#         else:
#             print(num_1+num_2)
#     if operation == "-":
#         try:
#             num_1 = int(input("введите число 1 "))
#             num_2 = int(input("введите число 2 "))
#         except ValueError:
#             print("неизветное значение")
#         else:
#             print(num_1-num_2)
#     if operation == "D":
#         try:
#             num_1 = int(input("введите число 1 "))
#             num_2 = int(input("введите число 2 "))
#             num_3 = int(input("введите число 3 "))
#         except ValueError:
#             print("неизветное значение")
#         else:
#             print(num_2*num_2-4*num_1*num_3) 




# from tkinter import * 
# window = Tk()
# window.geometry("800x600") 

# canvas = Canvas(window, width=800, height=600, bg="black")
# canvas.pack() 

# # canvas.create_rectangle(10, 10, 30, 30, fill = "yellow", outline="blue")
# # canvas.create_rectangle(40, 40, 80, 80, fill = "yellow", outline="blue")
# # canvas.create_rectangle(90, 90, 150, 150, fill = "yellow", outline="blue")
# canvas.create_polygon(10, 260, 60, 200, 110, 260, fill = "yellow", outline = "")
# canvas.create_rectangle(20, 260, 100, 330, fill = "yellow", outline="blue")



# window.mainloop()




# class Unit:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#     def sayHello(self):
#         print("Hi! My name is", self.name)


#     def pistol(self, other):
#         damage = 1000
#         print(self.name, "did pew-pew")
#         other.health = other.health - damage

# unit_1 = Unit("NAVI/MMA", 4500)
# unit_2 = Unit("GuilleVGX", 5000)

# print("здоровье GuilleVGX до: ", unit_2.health) 
# unit_1.pistol(unit_2)
# print("здоровье GuilleVGX после: ", unit_2.health) 

# unit_1.sayHello()
# unit_2.sayHello() 

# print(unit_1.health)
# print(unit_2.health) 



# from tkinter import * 

# class Image(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#         self.master.title("прямоугольники и треугольники")
#         self.pack(fill = BOTH, expand = True) 
#         canvas = Canvas(self) 
#         canvas.create_rectangle(10, 10, 30, 30, fill = "yellow", width=2)
#         canvas.create_rectangle(40, 40, 80, 80, fill = "yellow", width=2)
#         canvas.create_rectangle(90, 90, 150, 150, fill = "yellow", width=2)
#         canvas.create_polygon(10, 260, 60, 200, 110, 260, fill = "yellow", width=2)
#         canvas.create_rectangle(20, 260, 100, 330, fill = "yellow", width=2)
#         canvas.pack(fill = BOTH, expand = True) 
# window = Tk()
# f = Image() 
# window.geometry("800x600") 
# window.mainloop()  



# import random
# class Unit:
#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health 
   
#     def pistol(self, other):
#         damage = 10
#         print(self.name, "did pew-pew")
#         other.health = other.health - damage

# warriors = [Unit('GuilleVGX'), Unit('NAVI/MMA')]
# while True:
#     q = input('Введите 1, чтобы какой-то воин атаковал.')
#     if q == '1':
#         i = random.randint(0, 1)
#         attacker, victim = warriors[i], warriors[i - 1]
#         attacker.pistol(victim)
#         print(attacker.name, 'атаковал', victim.name)
#         print('У', victim.name, 'осталось здоровья', victim.health)
#         if victim.health <= 0:
#             print(attacker.name, 'победил!!!')     
#             break
#     elif q == '2':
#         break
#     else:
#         print('Ошибка ввода')



