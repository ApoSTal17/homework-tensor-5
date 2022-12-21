
# Задание 3

def fibonacci(n):
    """Функция вычисления чисел Фибоначчи

    args:
        n - номер числа Фибоначчи
    returns:
        Число Фибоначчи по номеру n
    """
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


try:
    number = int(input('Введите номер числа Фибоначчи (целое число): '))
    if number < 1:
        print('Число не должно быть меньше 1!')
    else:
        print(f'Результат: {fibonacci(number)}')

except ValueError:
    print('Неверный формат числа.')
