# объявление функции
def convert_to_python_case(text):
    newShit = list()

    for i in range(len(text)):
        if i == 0:
            newShit.append(text[i].lower())
        elif text[i].isupper():
            newShit.insert(i, '_'+text[i].lower())
        else:
            newShit.append(text[i].lower())

    newShit = ''.join(newShit)
    return newShit


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
