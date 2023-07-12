# 1. Тернарный условный оператор(if)

# age = 17
# is_allow = False

# if age >= 18:
#     is_allow = True
# else:
#     is_allow = False
# print(is_allow)


# age = 17
# is_allow = age>=18
# print(is_allow)

# ____________

# value = None
# if value is None:
#     res = []
# else:
#     res = value
# print (res)


# value = None
# res = [] if value is None else value
# print (res)

# 2. Генератор списков 

# div_5_list = [] #Все кратные 5 элементы от 0 до 100
# for x in range(100):
#     if x % 5 == 0:
#         div_5_list.append(x)
#     if x > 50:
#         x * 3
# print(div_5_list)


# div_5_list = [x**3 if x >50 else x for x in range(100) if x %5 == 0] 
# print(div_5_list)

#Cамостоятельное задание

# div_30_31_list = [x for x in range(250) if x % 30 == 0 or x % 31 == 0] 
# print (div_30_31_list)

#3. Генератор словарей

# words = ["red","orange","blue", "pink"]
# some_dict = {x: len(x) for x in words}
# print (some_dict["red"])


# def y(x):
#     return x**2 + 1
# some_list = [3284,238,38267,8927,-123]
# some_dict = {x: y(x) for x in some_list}
# print(some_dict)

#4. Кортежи

# a = "15"
# a = int(a) 


# some_tuple = (1, 2, 3, 4)
# print(some_tuple) 
# some_list = list(some_tuple)
# print(some_list)
# some_list.append(15)
# print(some_list)
# some_tuple = tuple(some_list) 
# print(some_tuple) 


# some_tuple = tuple(x for x in range(100))
# print(some_tuple)

#5. *args, **kwargs:

# def func (a, b):
#     print(a+b)
# func(2,2)


# def Label(a,b,*args,**kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs["bg"])
# label = Label(2,3, bg = "orange", font = "arial") 


# even_numbers = []
# odd_numbers = []

# for i in range(10):
#     number = int(input("Введите число: "))
#     if number % 2 == 0:
#         even_numbers.append(number)
#     else:
#         odd_numbers.append(number)

# print("Четные числа:", even_numbers)
# print("Нечетные числа:", odd_numbers)


# a = (5, 3, 2, 1, 4) 
# b = tuple(sorted(a, key=tuple)) 
# print('Исходный кортеж:', a) 
# print('Отсортированный кортеж:', b)



















                                                #УРОК 10

# import random

# class Tank:
#     def __init__(self, model,  health, armor, min_damage, max_damage):
#         self.model = model
#         self.health = health
#         self.armor = armor
#         self.damage = random.randint(min_damage, max_damage)
    
#     def print_info(self):
#         print(self.model, "имеет", self.health, "hp и", self.damage, "damage")

#     def health_down(self, enamy_damage):
#         self.health -= enamy_damage
#         print(self.model)
#         print("Танк повреждён!y него осталось", self.health, "hp")

#     def shot(self, enemy):
#         if enemy.health <=0 or self.damage >= enemy.health:
#             enemy.health = 0
#             print(enemy.model, "уничтожен")
#         else:
#             print()
#             print(self.model)
#             print("Есть пробитие в", enemy.model, "нанесено", self.damage, "hp")
#             enemy.health_down(self.damage)
    
# class SuperTank(Tank):
#     def __init__(self, model, health, armor, min_damage, max_damage, forseArmor):
#         super().__init__(model, health, armor, min_damage, max_damage)
#         self.forseArmor = forseArmor
    
#     def health_down(self, enamy_damage):
#         super().health_down(enamy_damage//2)

# tank1 = Tank("t-34", 100, 50, 10, 50)
# tank2 = Tank("Maus", 300, 100, 30, 60) 
# sTank = Tank("Ratte", 1000, 300, 50, 90)


# sTank.print_info()
# tank1.print_info()
# tank2.print_info()

# tank2.shot(sTank)




# class A:
#     def one(self):
#         print(1)
#     def two(self):
#         print(2)

# class B(A):
#     def two(self):
#         print("two")
#     def three(self):
#         print(3) 


# a = A()
# a.one()

# b = B()
# b.two() 







# class User:
#     def __init__(self, health):
#         self.health = health

# def attack(self, target):
#     pass 

# def take_damage(self, damage):
#     self.health -= damage 
 

# class Mage(User):
#     def __init__(self, health, mana):
#         super().__init__(health)
#         self.mana = mana

# def cast_spell(self, spell_name, target):
#     if self.mana >= spell_name.mana_cost:
#         spell_name.cast(target)
#         self.mana -= spell_name.mana_cost
#     else:
#         print("Not enough mana to cast spell")


# class Warrior(User):
#     def __init__(self, health, strength):
#         super().__init__(health)
#         self.strength = strength

# def attack(self, target):
#     damage = self.strength
#     target.take_damage(damage)


# class Archer(User):
#     def __init__(self, health, agility):
#         super().__init__(health)
#         self.agility = agility

# def attack(self, target):
#     damage = self.agility
#     target.take_damage(damage)