from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="

def getCourse(id):
    response = requests.get(url)
    xml = BeautifulSoup(response.content, "html.parser")
    valute = xml.find("valute", {"id": id})
    return valute.value.text


window = Tk()
window.geometry("410x400")
window.title("BANK")
title = Label(window, text=" Курс валют\n Банк", bg="orange", font="Arial 22")
title.place(y=40,x=170)

img_logo = PhotoImage(file="C:/Users/abalc/OneDrive/Изображения/ing/russiaa.png")
logo = Label(window, image=img_logo)
logo.place(x=0, y=0)

today = datetime.today()
today = today.strftime("%d/%m/%Y")

usd_label = Label(window, text="Курс на " + today, font="Arial 14")
usd_label.place(y=160,x=120)


usd_label = Label(window, text="$" + getCourse("R01235"), bg="green", font="Arial 14")
usd_label.place(y=200,x=60)

eur_label = Label(window, text="€" + getCourse("R01239"), bg="blue", font="Arial 14")
eur_label.place(y=200,x=180)

yua_label = Label(window, text="元" + getCourse("R01375"),bg="red", font="Arial 14")
yua_label.place(y=200,x=270) 

def converte():
    res = int(input_value.get()) * float(getCourse("R01235").replace(",", "."))
    result["text"] = res

input_value = Entry(window, width=10)
input_value.place(x=30, y=310)


btn = Button(text="Конвентировать!", background="#555", font="Arial 12", command=converte)
btn.place(x=120, y=305)

result = Label(window, text="Введите\nсумму", font="Arial 12")
result.place(x=280, y=300)


window.resizable(width=False, height=False)

window.mainloop()