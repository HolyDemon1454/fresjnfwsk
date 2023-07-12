#Простая реализация работника

# name = "Данила"
# salary = 200000
# print("y", name,"зарплата в месяц =", salary)
# print(f"У {name} зарплата в месяц = {salary}")



#Реализация в виде словаря 1 сотрудник:

# employee = {
#     "name": "Данила",
#     "salary": 200000
# }
# print(f"У {employee['name']} зарплата в месяц = {employee['salary']}")



# Реализация ввиде словоря много сотрудников

# employee_list = [1, 2321, 12321, 65743]

# employee_list = [
#     {
#     "name": "Данила",
#     "salary": 200000
#     },
#     {
#     "name": "Олег",
#     "salary": 150000
#     },
#     {
#     "name": "Гриша",
#     "salary": 2
#     }
# ]


# for employee in employee_list:
#     print(f"У {employee['name']} зарплата в месяц = {employee['salary']}")



# # Увольнение сотрудника

# print("\n** УВОЛЬНЯЕМ СОТРУДНИКА **")
# name = input("Введите кого увольнять: ") 
# for employee in employee_list:
#     if employee["name"] == name:
#         employee_list.remove(employee)

# print()
# for employee in employee_list:
#     print(f"У {employee['name']} зарплата в месяц = {employee['salary']}")



# # Нанимаем сотрудника

# print("\n** НАНИМАЕМ СОТРУДНИКА **")
# name = input("Введите имя сотрудника: ")
# salary = input("Введите ЗП сотрудника: ")
# new_employee = {
#     "name": name,
#     "salary": salary
# }
# employee_list.append(new_employee)

# print()
# for employee in employee_list:
#     print(f"У {employee['name']} зарплата в месяц = {employee['salary']}")



#Реализация через ООП

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.on_vacatin = False
        self.is_good_employee = 
    def get_info(self):
        return f"У {self.name} зарплата в месяц = {self.salary}"
    def on_vacation(self):
        self.on_vacatin = False


employee_list = [Employee("Данил", 0000), Employee("Олег", 150000), Employee("Петя", 6), Employee("Вася", 3), Employee("Генадий", 1000000)]

for employee in employee_list:
    print(employee.get_info()) 
