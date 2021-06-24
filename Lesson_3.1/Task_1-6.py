# Решение заданий 1-6:
# 
# 
from random import randint
list_a = list()
list_b = list()
list_c = list()
[list_a.append(randint(0,7)) for i in range(1, 7)]
[list_b.append(randint(1,5)) for i in range(1, 7)]
[list_c.append(randint(3,9)) for i in range(1, 7)]
print(f"List_a: {list_a}")
print(f"List_b: {list_b}")
print(f"List_c: {list_c}")
# 
# 
# ============Функция произведения элементов списка целых:============
# 
# 
def multiplication(list_a):
    x = 1
    for i in list_a:
        if i != 0:
            x += 1
        else:
            x == 0
            print("Произведение элементов списка = 0!")
            break
    return f"Произведение элементов списка целых: {x}"
print(multiplication(list_a))
# Итог: 
# Произведение элементов списка целых: 7
# 
# 
# ============Функция минимума элементов списка целых:============
# 
# 
def minimum(list_b):
    return f"Минимальное значение списка: {min(list_b)}"
print("Минимальное значение списка:", min(list_b))
# Итог: 
# Минимальный элемент списка: 2
# 
# 
# ============Функция нахождения количества простых чисел в списке:============
# 
# 
def simple(list_c):
    y = 0
    for i in list_c:
        if all(i % j != 0 for j in range(1, i)):
            y += 1
    return f"Kоличество простых чисел в списке целых: {y}"
print(simple(list_c))
# Итог: 
# Kоличество простых чисел в списке целых: 0  ?????????
# 
# 
# ============Функция, которая удаляет из списка заданное число:============
# 
# 
def del_ete(list_b, list_c):
    z = 0
    for i in list_b:
        if i in list_c:
            list_b.remove(i)
            z += 1
    return f"Количество удаленных элементов: {z}"
print(del_ete(list_b, list_c))
# Итог: 
# Kоличество удалённых элементов: 3
# 
# 
# ============Функция, которая высчитывает степень каждого элемента:============
# 
# 
d = 3
def dee_gre(list_a, d):
    new_list = []
    for i in list_a:
        new_list.append(i**d)
    return f"Cписок, в котором элемент находится в степени 3: {new_list}"
print(dee_gre(list_a, d))
# Итог: 
# Cписок, в котором элемент находится в степени 3: [1, 64, 343, 27, 125, 343]
# 
# 
# ============Функция объединения списков============
# 
# 
def combi_list(list_a, list_c):
    return f"Cписок, объединяющий элементы двух списков: {list_a + list_c}"
print(combi_list(list_a, list_c))
# Итог: 
# Cписок, объединяющий элементы двух списков: [1, 0, 2, 1, 4, 5, 3, 5, 8, 3, 3, 4] 
# 
# 
