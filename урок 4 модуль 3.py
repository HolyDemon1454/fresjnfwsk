# my_list = [x for x in range(1,1000000)]
# print (my_list)

# my_list2 = (x for x in range(1,1000000))
# # print (my_list2)
# # print(next(my_list2))
# for i in my_list2:
#     print(i)

# def lazy_func():
#     for item in range(1, 11):
#         print("до", item)
#         yield item
#         print("после", item)
# print(next(lazy_func()))

# for i in lazy_func():
#     print(i) 


# f = open("test.txt","w")
# f.write("Hello")
# f.close()

# import contextlib


# with open("test.txt","w") as f:
#     f.write("Helloo")



# говорить = print
# привет = "привет"
# говорить(привет)


# import contextlib

# def decor(func):
#     def new_func():
#         print("newl")
#         func()
#         print("new2")
#     return new_func
# def my_func():
#     print("main")

# my_func = decor(func = my_func)

# import contextlib

# @contextlib.contextmanager
# def reverse_str(you_str):
#     print("вход к контекстный мэнеджер")
#     yield you_str[::-1]
#     print("выход из контекстного менеджера")

# with reverse_str("Hello world") as r:
#     print(r) 

# import contextlib

# @contextlib.contextmanager
# def exc_handler(exc):
#     try:
#         yield True 
#     except exc:
#         print("Произошло исключение") 

# with exc_handler(IndexError):
#     my_list = [1,2]
#     print(my_list[3]) 

# import time
# start = time.time()
# m2 = (time.sleep(x) for x in range(1,3))
# next(m2)
# end = time.time
# print(end-start)

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# func(1,2,3,4,5, a = 1,b = 2, c = 3) 


# def squares(maxn): return map((2).__rpow__, range(maxn + 1))

# def squares(maxn): return (x * x for range(maxn + 1))

# print(*squares(1000000))



# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# import contextlib
# url = " http://www.cbr.ru/scripts/XML_daily.asp ?"
# date = 'date_req=11/09/2002'
# today = datetime.today ()
# today = today.strftime('%d/%m/%Y')

# parload = {'date_req' : today}

# response = requests.get(url, params = parload)

# xml = BeautifulSoup(response.content, 'lxml')
# @contextlib.contextmanager
# def get_course_info(id):
#     return xml.find('valute', {'id': id}).value.text
# print(get_course_info("R01010"))



# print("(1 шт.) Австралийский доллар стоит(ят): ")

# with get_course_info("R01010") as corrency:
#     print(corrency)