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
import task1


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


num = task1.input_numbers("Задайте длинну списка: ")
used_list = task1.creates_list(num)
print(used_list)
result = multiplies_numbers(used_list)
print(f"произведение пар чисел списка: {result}")
