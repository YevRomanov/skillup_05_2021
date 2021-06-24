# # numbers = []
# # # Наполняем список от 0 до 9 с помощью range и метода append:
# # for i in range(10):
# #     numbers.append(i)

# # print(numbers)
# # # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # # Нужно найти значение из списка по его порядковому номеру 4
# # #  и вывести на экран:
# # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
# # to_find = 5
# # for number in my_list:
# #     print(number)
# #     if number == to_find:
# #         print("I've just found you:", number)

    
# # numbers = []
# # for i in range(10):
# #     numbers.append(i)
# # print(numbers)
# # # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # # Выводим в одну строчку, с помощью создания выражения внутри списка,
# # # которое каждый раз возвращает одно новое значение(например i):
# # numbers = [i for i in range(10)] 
# # # i слева - это значение, которое нужно записать в список numbers
# # print(numbers)
# # # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # numbers = [i*2 for i in range(10)] 
# # print(numbers)
# # # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# # marks = {
# #     "Maths": 
# # }

# # 




# a = 10
# b = 20
# if (a < b):
#     print("a < b. It's true")

# username = "dima"
# password = "password"

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# if username_input == username and password_input == password:
#     print("Success auth")


# # Functions
# def greeting(name):
#     print('Hello', name)

# greeting('Yuliia')
# greeting('Dima')

# def parabola(x):
#     print(x**2)

# parabola(2)
# parabola(-2)

# from pprint import pprint

# players = [
#     {
#         "name": "John Doe",
#         "heigh": 2.1
#     },
#     {
#         "name": "Peter Parker",
#         "heigh": 1.9
#     },
#     {
#         "name": "Tonny Stark",
#         "heigh": 2.0
#     },
# ]


# def add_player(name, heigh):
#     players.append({
#         "name": name,
#         "heigh": heigh
#     })


# def remove_player(name):
#     index = 0
#     for player in players:
#         if player["name"] == name:
#             del players[index]
#         else:
#             index += 1


# add_player("New player", 2.2)
# add_player("New player 2", 3.2)
# add_player("New player 3", 2.3)

# remove_player("Peter Parker")
# remove_player("New player 2")

# pprint(players)


def say_hello():
    print("Hello")

say_hello()