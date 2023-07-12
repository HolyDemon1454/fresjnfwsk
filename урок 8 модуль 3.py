# goods = [
#     {
#         "name": "Iphon 14",
#         "brand": "Apple",
#         "price": 1200
#     },
#     {
#         "name": "Galaxy A23",
#         "brand": "Samsung",
#         "price": 600
#     },
#     {
#         "name": "Note 10",
#         "brand": "Xiaomi",
#         "price": 400
#     },
#     {
#         "name": "Iphon 11",
#         "brand": "Apple",
#         "price": 900
#     }
# ]

# # def item_price(item):
# #     return item["price"]

# print(sorted(goods, key=lambda item:item["price"]))

# apple_list = filter(lambda item: item["brand"]=="Apple", goods)
# print(list(apple_list))



# a = ["1", "2", "3", "4"]
# # b = map(int, a)
# # print(b)

# def sss(item):
#     return item + "sss"

# print(list(map(sss, a))) 



# goods = [
#     {
#         "name": "Iphon 14",
#         "brand": "Apple",
#         "price": 1200
#     },
#     {
#         "name": "Galaxy A23",
#         "brand": "Samsung",
#         "price": 600
#     },
#     {
#         "name": "Note 10",
#         "brand": "Xiaomi",
#         "price": 400
#     },
#     {
#         "name": "Iphon 11",
#         "brand": "Apple",
#         "price": 900
#     }
# ]

# for i, item in enumerate(goods):
#     print(i, item)


# names = ["Артур", "Алексей", "Семён", "Данила"]
# surnames = ["Пирожков", "Шевцов", "Лабанов", "Поперечный"]
# favorit_object = ["Музыка", "Обществознание", "Биология", "Технология"]

# for name, surname in zip(names, surnames):
#     print(name, surname)

# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
 
#     def __repr__(self):
#         return self.brand
 
# items_list = [
#     Item(1000, "Apple"),
#     Item(1200, "Apple"),
#     Item(900, "Samsung"),
#     Item(700, "Samsung"),
#     Item(660, "Xiaomi")
#     ]

# result = list(filter(lambda x: x.brand == 'Apple', items_list)) 
# print(result) 
# for x in result: print(x.brand, x.price)


names_list = ['данил', 'артём', 'никита', 'влад'] 
print([x[0].upper() + x[1:] for x in names_list]) 

