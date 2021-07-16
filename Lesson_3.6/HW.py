#################   Task 1   #################   
# Дано два текстовых файла. Выяснить, совпадают ли их строки. 
# Если нет, то вывести несовпадающую строку из каждого файла.
# 
# 
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
# Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв; ■ Количество цифр.
# 
# 
letters_to_find = "aeiouy"

file_1 = "Lesson_3.6/text3.txt"
file_2 = "Lesson_3.6/text4.txt"

def get_file_lines(filename: str) -> list:
    with open(filename) as f:
        return f.readlines()

def count_vowels(source_list: list) -> int:


file1_lines = get_file_lines(file_1)
file2_lines = get_file_lines(file_2)




#################   Task 3   ################# 
# Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.


#################   Task 4   ################# 
# Дан текстовый файл. Найти длину самой длинной строки.


#################   Task 5   ################# 
# Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.
