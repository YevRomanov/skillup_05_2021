# Задание №3:
# Создание программы "ФИРМА"
from pprint import pprint
# Создаём базу данных работников: ФИО, телефон, рабочий email, название должности, номер кабинета, skype
workers_1 = {
    "Сергей Петров": [678901345, "s.petrov@gmail.com", "worker", 1, "Serzh"],
    "Вита Лекова": [452456789, "v.lekova@gmail.com", "secretar", 2, "Vita"],
    "Пётр Осипов": [123654765, "p.osipov@gmail.com", "boss", 3, "Petr_1"],
    "Катя Зекова": [908709809, "e.zekova@gmail.com", "manager", 4, "Katia_32"]
}
pprint(workers_1)
pprint(workers_1["Сергей Петров"])
# 
# 
print("==================Добавление==================")
new_worker = {
    "Валера Карпов": [678212345, "v.karpov@gmail.com", "worker", 1, "Valerka"],
}
workers_1.update(new_worker)
pprint(workers_1)
# 
# 
print("==================Удаление==================")
del workers_1["Катя Зекова"]
pprint(workers_1)
# 
# 
print("==================Замена==================")
workers_1["Вита Лекова"] = [454566789, "v.lekova@gmail.com", "manager", 2, "Vit_manager"]
pprint(workers_1)
# 
# 
print("==================Поиск==================")
search_p = input("Я ищу сотрудника, ФИО :")
if search_p in workers_1.keys():
    person = workers_1.get(search_p)
    print("Данные сотрудника:", {person[0]}, {person[1]}, {person[2]}, {person[3]}, {person[4]})
else:
    print("Данный сотрудник не найден в базе")