def task_5(number):
    text = str(number)
    if len(text) % 2 != 0:
        return False
    first_part = text[:len(text)//2]
    second_part = text[len(text)//2:]

    result = first_part == second_part[::-1]
    return result


result = task_5(1233214)
print(result)