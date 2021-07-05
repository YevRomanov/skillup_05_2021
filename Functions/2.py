# def header(func):

#     def inner(*args, **kwargs):
#         print("<h1>")
#         func(*args, **kwargs)
#         print("</h1>")
#     return inner

# def table(func):

#     def inner(*args, **kwargs):
#         print("<table>")
#         func(*args, **kwargs)
#         print("</table>")
#     return inner


# @header # say = header(say)
# @table
# def say(name, surname, age):
#     print("hello", name, surname, age)

# say('Vasya', 'Ivanov', 30)

import time 

def testTime(fn):
    def wrapper(*args):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")
    return wrapper

