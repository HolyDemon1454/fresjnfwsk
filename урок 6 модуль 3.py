# class Year:
#     def __init__(self):
#         self.__days = 365
#     def get_days(self):
#         return self.__days
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception("некорректное значение!")

# year1 = Year()
# year1.set_days(365)
# print(year1.get_days())

class Person:
    def __init__(self, name, age, deleter):
        self.name = name
        self.age = age
    
    @property 
    def deleter(self): 
        return self.__deleter
    @deleter.setter  
    def name(self, deleter):
        self.__deleter = deleter

    @property 
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name


    @property 
    def age(self):
        return self.__age 
    @age.setter
    def age(self, age):
        if age>= 0:
            self.__age = age
        else:
            raise Exception("Вы ещё не родились!")


person = Person("Иван", 25)
person.age = -5
print(person.age)