# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import sample

def input_numbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Это не число!")
    return number


def creates_list(number):
    list_nums = sample(range(1, number * 5), number)
    return list_nums


def find_sum_elements(used_list):
    result = 0
    for i in range(0, len(used_list), 2):
        result += used_list[i]
    return result

num = input_numbers("Задайте длинну списка: ")
used_list = creates_list(num)
print(used_list)
print(f"сумма элементов списка, стоящих на нечётных позициях равна: {find_sum_elements(used_list)}")
