# При помощи данной ф-и можно обходить элементы коллекции
# Берем список из 4-х элементов в качестве коллекции:

a = [10, 20, 30, 40, 50, 60]
# print(enumerate(a))
# Превращаем объект в список с помощью ф-и list:
# print(list(enumerate(a)))
# [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50), (5, 60)]
for para in enumerate(a):
    print(para)

for index, value in enumerate(a):
    if value%20==0:
        print(index, value)

# Увеличение значения каждого элемента списка:
for index, value in enumerate(a):
    a[index]+=1
print(a)
# [11, 21, 31, 41, 51, 61]


s = "hello"
for index, value in enumerate(s):
    print(index, value)
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o

t = ("apple", "banana", "mango")
for index, value in enumerate(t):
    print(index, value)
# 0 apple
# 1 banana
# 2 mango

d = {"a":1, "b":2, "c":3}
for index, value in enumerate(d):
    print(index, value)
# 0 a
# 1 b
# 2 c


# Так же можно передать ф-ю range, которая генерирует коллекцию:
for index, value in enumerate(range(10, 20)):
    print(index, value)
# 0 10
# 1 11
# 2 12
# 3 13
# 4 14
# 5 15
# 6 16
# 7 17
# 8 18
# 9 19


# Особенность ф-и enumerate, которая позволяет изменить порядковый номер:
 t = ("apple", "banana", "mango")
for index, value in enumerate(t):
    print(index, value)