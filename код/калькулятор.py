# 5923726444: AAFzro1TD8ZMOzD-AwQC4qXUaVtHikPVe_s

# import telebot
# import random
# token = "5923726444:AAFzro1TD8ZMOzD-AwQC4qXUaVtHikPVe_s"
# bot = telebot.TeleBot(token) 

# @bot.message_handler(commands=["start", "help"])
# def send_wecome(message):
#     welcome = "Привет, я чертила а не бот. Могу ответить, а могу не ответить (/start /help /pcem /cat /igra)"
#     keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
#     button1 = telebot.types.KeyboardButton("Анекдот")
#     button2 = telebot.types.KeyboardButton("кот")
#     keyboard.add(button1, button2,) 
#     bot.send_message(message.chat.id, welcome, reply_markup=keyboard)

# @bot.message_handler(commands=["cat"])
# def send_cat(message):
#     # cat_number = str(random.randint(1,9))
#     # cat_ing = open("ing/" + cat_number + ".jpg", "rb")
#     # bot.send_photo(message.chat.id, cat_ing)
#     cat_ing = open("ogon_1.jpg", "rb")
#     bot.send_photo(message.chat.id, cat_ing)


# @bot.message_handler(commands=["pcem"])
# def send_pcem(message):
#     pcem = "внимание анекдот: появился как то в зоне чёрный сталкер..................."
#     bot.send_message(message.from_user.id, pcem)

# @bot.message_handler(commands=["igra"])
# def send_igra(message):
#     igra = "игру в каком жанре вы хотите?"
#     bot.send_message(message.from_user.id, igra)   
    
#     keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
#     button_url = telebot.types.InlineKeyboardButton("Перейти", url="https://vk.com/id536682921")
#     keyboard.add(button_url)
#     bot.send_message(message.chat.id, "Настя", reply_markup=keyboard)


# @bot.message_handler(commands=["sticker"]) 
# def send_sticker(message):
#     bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHMlhjvYz_rGHiEj1y5gW2QUuULQABGmcAApwAA8O54TBtE1GyieH6Qi0E")


# @bot.message_handler(content_types=["text"])
# def get_text_message(message):
#     if message.text.lower() == "привет":
#         bot.send_message(message.from_user.id, "Салам")
#     if message.text.lower() == "пока":
#         bot.send_message(message.from_user.id, "бб")
#     if message.text == "Анекдот":
#         send_pcem(message) 
#     if message.text.lower() == "кот":
#         send_cat(message)
#     if message.text.lower() == "экшен":
#         bot.send_message(message.from_user.id, "Майнкрафт")  
#     else:
#         bot.send_message(message.from_user.id, "я не знаю таких слов")



# bot.polling()  



# Подключаю к программе модуль для работы с окнами 


# import random

# class Warrior:
#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health

#     def hit(self, target):
#         if type(self) == type(target):
#             target.health -= 20
#         else:
#             raise TypeError

# warriors = [Warrior('Воин1'), Warrior('Воин2')]
# while True:
#     q = input('Введите 1, чтобы какой-то воин атаковал. Для закрытия программы введите 2: ')
#     if q == '1':
#         i = random.randint(0, 1)
#         attacker, victim = warriors[i], warriors[i - 1]
#         attacker.hit(victim)
#         print(attacker.name, 'атаковал', victim.name)
#         print('У', victim.name, 'осталось здоровья', victim.health)
#         if victim.health <= 0:
#             print(attacker.name, 'победил!!!')
#             break
#     elif q == '2':
#         break
#     else:
#         print('Ошибка ввода')