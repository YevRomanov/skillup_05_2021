# numbers = []
# # Наполняем список от 0 до 9 с помощью range и метода append:
# for i in range(10):
#     numbers.append(i)

# print(numbers)
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Нужно найти значение из списка по его порядковому номеру 4
# #  и вывести на экран:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
# to_find = 5
# for number in my_list:
#     print(number)
#     if number == to_find:
#         print("I've just found you:", number)

    
# numbers = []
# for i in range(10):
#     numbers.append(i)
# print(numbers)
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Выводим в одну строчку, с помощью создания выражения внутри списка,
# # которое каждый раз возвращает одно новое значение(например i):
# numbers = [i for i in range(10)] 
# # i слева - это значение, которое нужно записать в список numbers
# print(numbers)
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# numbers = [i*2 for i in range(10)] 
# print(numbers)
# # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# marks = {
#     "Maths": 
# }

a = [1, 2, 3, 4]
tpl = (1, 2, 3, 4)
print(a.__sizeof__())
print(tpl.__sizeof__())

def get_user():
    name = "Alex"
    age = 27
    admin = False
    return name, age, admin

user = get_user()
print(user[0])
print(user[1])
print(user[2])

user = ("Alex", 27, False)

name = "Alex"
if name in user:
    print("Пользователь найден:", name)
else:
    print("Пользователь не найден")