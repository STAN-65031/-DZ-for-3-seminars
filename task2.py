# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
from random import sample

def input_numbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
            if number == 0:
                okey = False
                print("Список не может быть равен 0")
        except ValueError:
            print("Это не число!")
    return number


def creates_list(number):
    list_nums = sample(range(1, number * 5), number)
    return list_nums

def multiplies_numbers(used_list):
    multiply_numbers = []
    counter = len(used_list)
    if counter % 2 == 0:
        for i in range(int(counter/2)):
            multiply_numbers.append(used_list[i] * used_list[counter - 1 - i])
    else:
        for i in range(int((counter+1)/2)):
            multiply_numbers.append(used_list[i] * used_list[counter - 1 - i])
    multiply_numbers.pop(-1)
    center = used_list[int((counter+1)/2-1)]
    multiply_numbers.append(center)


    return multiply_numbers


num = input_numbers("Задайте длинну списка: ")
used_list = creates_list(num)
print(used_list)
result = multiplies_numbers(used_list)
print(f"произведение пар чисел списка: {result}")
