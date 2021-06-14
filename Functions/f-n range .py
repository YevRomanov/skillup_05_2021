# С помощью функции range можно сформировать конечную
# арифметическую прогрессию!

x = range(5)
print(x)
print(type(x))

# Оборачиваем range в функцию list, чтобы увидеть арифметическую прогрессию:

print(list(x))
print(list(range(17)))
print(list(range(11)))
print(list(range(3)))
print(list(range(10,25)))
print(list(range(10,5))) 

# Изменение шага в range с помощью трёъ параметров:
# list(range(start, end, шаг))

print(list(range(1, 100, 2)))
print(list(range(1, 101, 10)))   
print(list(range(1, 102, 10)))   
print(list(range(10, 0, -1))) 
print(list(range(10, -2, -1))) 

# То есть, можем использовать ф-ю range
# в трёх случаях:
# - передаём один параметр:
print(list(range(10)))
# - передаём два параметра:
print(list(range(10, 20)))
# - передаём три параметра:
print(list(range(0, 100, 3)))


# Сумма арифмитеческой прогресии:
print(sum(range(1, 101)))
print(sum(range(1, 5)))

# Определение длинны(к-ва элементов) списка:
print(len(range(5, 16, 5)))
print(len(range(1, 33)))

# Конструкция множественного присвоения:
a, b, c = range(5, 8)
print(a)
print(b)
print(c)

# Сохранение результата ф-и в переменную:
r = range(1, 7)
print(len(r))
print(r[1])


# Объект ф-и range является итерируемым(iterable)-
# это объект, предоставляющий возможность прохода по своим элементам:
v = iter(range(5))
print(v)
print(next(v))
print(next(v))
print(next(v))
print(next(v))

n = iter([43, True, "Hello"])
print(next(n))
print(next(n))
print(next(n))

