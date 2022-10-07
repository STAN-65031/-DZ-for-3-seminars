
# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011


def input_numbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Это не число!")
    return number


def converts_binary(number):
    list_numbers = []
    while number > 0:
        list_numbers.insert(0, number % 2)
        number //= 2
    return list_numbers


num = input_numbers("Введите натуральное число: ")
binary = converts_binary(num)
print(int(''.join(map(str, binary))))