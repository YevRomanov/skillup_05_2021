# Генераторы списков /  List comprehension
# [выражение for value in коллекция]

a = [0 for i in range(2)]
print(a)
b = [1 for i in range(5)]
print(b)
c = [i for i in range(10)]
print(c)
d = [i**2 for i in range(2, 7)]
print(d)
e = [i%4 for i in range(1, 15)]
print(e)

f = [i*4 for i in "hello"]
print(f)
g = [i for i in "hello"]
print(g)


# Функция ord находит код в таблице ascii:

h = [ord(i) for i in "abcd"]
print(h)


# Функция-генератор randint(рандом):
import random

l = [random.randint(-10, 10) for i in range(10)]
print(l)
# Отбрасываем отрицательные значения с помощью abs:
k = [abs(elem) for elem in l]
print(k)
# Увеличиваем все значения списка l на +1:
s = [elem+1 for elem in l]
print(s)
# Умножаем все значения списка l на 2:
j = [elem*2 for elem in l]
print(j)



# В генераторах списка можно также использовать условные конструкции
# [выражение for value in коллекция if условие]

p = [random.randint(-10, 10) for i in range(10)]
print(p)
# В отдельном списке o ставляем только чётные элементы списка p:
o = [elem for elem in p if elem%2==0]
print(o)


# Вывод нескольких чисел через пробел в одну строку:
a 





