# Создать множества: A, B, C з любыми элементами.
# Найти: 
# 1. Различне элементы для A и B. 
# 2. Одинаковые элементы для A и C.
# 3. Объединение 3-х множеств.
from pprint import pprint
# 
# 
# Создаём множества A, B, C:
A = {1, 3, "hello", 7, 9, False}
B = {1, "bye", 2, None, 5, 8, True}
C = {False, "good",1, 0, 2, None, 5, 9, "morning"}
print(3 in A)
print(None not in B)
print(9 in C)
# 
# 
print("==================Находим различные элементы для A и B:==================")
print(A.isdisjoint(B))
print(B.isdisjoint(A))
print(A.difference(B))
print(B.difference(A))
# 
# 
print("==================Находим одинаковые элементы для A и С:==================")
print(A & C)
# 
# 
print("==================Объединяем множества A, B, С:==================")
print(A ^ B ^ C)

