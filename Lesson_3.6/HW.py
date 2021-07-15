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
text_file = 
