# import requests
# from bs4 import BeautifulSoup

# url = "https:/www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/"

# def getCourse(id, year):
#     response = requests.get(url + str(year))
#     xml = BeautifulSoup(response.content, "html.parser")
#     valute = xml.find("valute", {"id": id})
#     return valute.value.text

# year = input("Введите год (например:2015): ")
# print(getCourse("R01239", year))


# def convert(from_valute, to_valute, value):
#     rub = from_valute.course * value
#     valute = rub / to_valute.course
#     return valute

# dict = {
#     "EUR": "R01239",
#     "KZT": "R01335",
#     "USD": "R01235",
#     "AZN": "R01020A",
#     "GBP": "R01035",
# }

# convert(dict["AZN"], dict["GBP"])

# arr = xml.find_all("valute") 
# print(arr[0].name.text) 
# for i in arr:
#     print(i.charcode.text, i.value.text)


import requests
from bs4 import BeautifulSoup

url = "https:/www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/"

def getCourse(id, year):
    response = requests.get(url + str(year))
    xml = BeautifulSoup(response.content, "html.parser")
    valute = xml.find("valute", {"id": id})
    return valute.value.text

year = input("Введите год (например:2015): ")
print(getCourse("R01239", year))

valute_from = "EUR" 
valute_to = "USD" 
amount = int(input("Enter the amount to be converted: ")) 
 
def course(valute_from, valute_to, amount): 
    rates = {
        "USD": "R01235",
        "EUR": "R01239"
    } 
     
    if valute_from == "EUR": 
        return amount / rates[valute_to] 
    else: 
        return amount / rates[valute_from] * rates[valute_to] 
 
print("Converted amount:", course(valute_from, valute_to, amount))