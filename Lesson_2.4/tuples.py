# ==============================КОРТЕЖИ==============================
# Задание 1. Есть три кортежа целых чисел необходимо найти элементы, которые есть во всех кортежах.
# Задание 2. Есть три кортежа целых чисел необходимо найти элементы, которые уникальны для каждого списка.
# Задание 3. Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и 
# находятся в каждом из кортежей на той же позиции.
# 
# 
a = (0, 1, 3, 5, 7, 9)
b = (0, 2, 4, 5, 8)
c = (2, 3, 4, 5, 6, 7, 8)
print(a, b, c)
# 
# 
print("=================Элементы, которые есть во всех кортежах:===================")
abc = tuple(set(a) & set(b) & set(c))
print("Элемент", abc, "- общий для всех кортежей")
# 
# 
print("=================Элементы, которые уникальны для каждого списка:===================")
diff_abc_1 = list(set(a) - set(b) - set(c))
diff_abc_2 = list(set(b) - set(a) - set(c))
diff_abc_3 = list(set(c) - set(b) - set(a))
print(diff_abc_1)
print(diff_abc_2)
print(diff_abc_3)
# 
# 
print("=================Элементы, которые есть в каждом из кортежей и на той же позиции:===================")
print(a[2])
print(b[2])
print(c[2])