# ========== Два списка целых случайных чисел: ==========

from random import randint

my_list_1 = sorted([randint(1, 55) for i in range(7)])
my_list_2 = sorted([randint(1, 99) for i in range(7)])

print("Первый список целых чисел:", my_list_1)
print("Второй список целых чисел:", my_list_2)

#========== Третий список, содержащий элементы обоих списков: ==========

my_list_3 = my_list_1 + my_list_2

print("Третий список целых чисел:", my_list_3)

#========== Четвёртый список, содержащий элементы общие для двух списков ==========

my_list_4 = sorted(list(set(my_list_3)))

print("Четвёртый список целых чисел:", my_list_4)

#========== Пятый список, содержащий элементы общие для двух списков ==========

my_list_5 = set(my_list_1) & set(my_list_2)

print("Пятый список целых чисел:", my_list_5)

#========== Шестой список, содержащий только уникальные элементы каждого из списков ==========

my_list_6 = sorted(list(set(my_list_1) - set(my_list_2)) + list(set(my_list_2) - set(my_list_1)))

print("Шестой список целых чисел:", my_list_6)

#========== Седьмой список, содержащий только минимальное и максимальное значение каждого из списков ==========

my_list_7 = []
my_list_7.append(min(my_list_1))
my_list_7.append(min(my_list_2))
my_list_7.append(max(my_list_1))
my_list_7.append(max(my_list_2))

print("Седьмой список целых чисел:", my_list_7)

# ============================================================================================================
Первый список целых случайных чисел: [1, 7, 15, 22, 22, 29, 49]
Второй список целых случайных чисел: [7, 10, 66, 76, 83, 84, 89]
Третий список, содержащий элементы обоих списков: [1, 7, 15, 22, 22, 29, 49, 7, 10, 66, 76, 83, 84, 89]
Четвёртый список, содержащий элементы общие для двух списков: [1, 7, 10, 15, 22, 29, 49, 66, 76, 83, 84, 89]
Пятый список, содержащий элементы общие для двух списков: {7}
Шестой список, содержащий только уникальные элементы каждого из списков: [1, 10, 15, 22, 29, 49, 66, 76, 83, 84, 89]
Седьмой список, содержащий только минимальное и максимальное значение каждого из списков: [1, 7, 49, 89]
# ============================================================================================================










