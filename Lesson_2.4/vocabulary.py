# Задание №2:
# Создание программы, "англо-французский словарь"
from pprint import pprint
vocab_1 = {
    "hi": "salut",
    "you": "toi",
    "how": "comment",
    "here": "ici",
    "i": "je",
    "we": "nous"
}
pprint(vocab_1)
pprint(vocab_1["hi"])
# 
# 
print("==================Добавление слова в словарь==================")
new_word = {
    "hide": "cacher"
}
vocab_1.update(new_word)
pprint(vocab_1)
# 
# 
print("==================Удаление слова из словаря==================")
del vocab_1["you"]
vocab_2 = vocab_1.pop("i")
pprint(vocab_1)
pprint(vocab_2)
# 
# 
print("==================Замена слова в словаре==================")
pprint(vocab_1["here"])
vocab_1["here"] = "doit"
pprint(vocab_1)
# 
# 
print("==================Поиск слова в словаре==================") 
to_find = input("Введите слово для поиска: ")
if to_find in vocab_1:
    print("Слово", to_find, "уже было в словаре")
else:
    print("Слова", to_find, "в словаре не найдено")
