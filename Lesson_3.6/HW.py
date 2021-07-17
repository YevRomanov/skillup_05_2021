#################   Task 1   #################   
# Дано два текстовых файла. Выяснить, совпадают ли их строки.#
# Если нет, то вывести несовпадающую строку из каждого файла.#
# 
# 
from typing import List

stream_1 = open('Lesson_3.6/text1.txt', mode="r")
stream_2 = open('Lesson_3.6/text2.txt', mode="r")
def compare(file_1, file_2):  
    lines_1 = stream_1.readlines() 
    lines_2 = stream_2.readlines() 
    dif = []
    for l in lines_1:
        if l not in lines_2:
            dif.append(l)
            return dif
print(f'Mismatched strings: {compare(stream_1, stream_2)}')
stream_1.close()
stream_2.close()
# 
# 
# Mismatched strings: ["'''Today, Silicon Valley is still the home of the computer industry; \n"]
# 
# 
# 
# 
# 
#################   Task 2   #################  
# Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:#
# ■ Количество символов;#
# ■ Количество строк;#
# ■ Количество гласных букв;#
# ■ Количество согласных букв; ■ Количество цифр.#
# 
# 
# letters_to_find_1 = "aeiouy"
# letters_to_find_2 = "qwrtpsdfghjklzxcvbnm"
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# file_1 = "Lesson_3.6/text3.txt"
# file_2 = "Lesson_3.6/text4.txt"

# def get_file_lines(filename: str) -> list:
#     with open(filename) as f:
#         return f.readlines()

# def count_vowels(text: str) -> list:
#     counter = 0
#     for i in text:
#         if i in letters_to_find_1:
#             counter += 1 
#     return counter

# def count_digits(filename: int) -> list:
#     with open(filename) as f:
#         return f.readlines()

# def count_consonants(text: str) -> int:
#     counter = 0
#     for i in text:
#         if i in letters_to_find_2:
#             counter += 1 
#     return counter
    
# file1_lines = get_file_lines(file_1)
# file2_lines = get_file_lines(file_2)

# file1_chars = "".join(file1_lines)
# file2_chars = "".join(file2_lines)

# file1_vowels = count_vowels(file1_chars)
# file2_vowels = count_vowels(file2_chars)

# file1_consonants = count_consonants(file1_chars)
# file2_consonants = count_consonants(file2_chars)

# file1_digits = count_digits(file1_chars)
# file2_digits = count_digits(file2_chars)

# print("file1_vowels:", file1_vowels)
# print("file2_vowels:", file2_vowels)
# print("file2_consonants:", file1_consonants)
# print("file2_consonants:", file2_consonants)
# print("file1_digits:", file1_digits)
# print("file2_digits:", file2_digits)
# 
# 
# 
# 
# 
#################   Task 3   ################# 
# Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.#
# 
# 
with open("Lesson_3.6/text2.txt", mode = "r", encoding="utf-8") as f:
    text = f.readlines()
text.remove(text[-1])


with open("Lesson_3.6/text5.txt", mode = "a", encoding="utf-8") as file:
    for i in text:
        file.write(f"{i}")
# 
# 
# 
# 
#         
#################   Task 4   ################# 
# Дан текстовый файл. Найти длину самой длинной строки.#
# 
# 
# with open("Lesson_3.6/text1.txt", mode = "a", encoding="utf-8") as f:
#     text = f.readlines()

# for i in text:
#     max_l = 0
#     if len(i) > max_l:
#         max_l = len(i)
#         print(max_l)
# 
# 
# 
# 
#  
#################   Task 5   ################# 
# Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.#
# 
# 
file = open("Lesson_3.6/text6.txt", mode = "r", encoding="utf-8")
print(file)
    

# find_word = input()

# for i in find_word:
#     if i in text:
#         print(i)
