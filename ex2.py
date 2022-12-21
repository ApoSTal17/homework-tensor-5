
# Задание 2

def add(args):
    """Функция суммирования любого количества численных аргументов
    
    args:
        args - численные аргументы в любом количестве в виде списка или кортежа
    returns:
        Численную сумму аргументов args
    """
    return sum(args)

message = '''Выберите режим работы:
    1) 1 - Целочисленные параметры
    2) 2 - Вещественные параметры
    3) 3 - Выход из программы
    >>> '''

while True:
    try:
        var = int(input(message))

        if var == 1:
            decimal = map(int, input('Введите целочисленные параметры через пробел: ').split())
            print(f'Сумма целочисленных параметров = {add(decimal)}')
        if var == 2:
            real = map(float, input('Введите вещественные параметры через пробел: ').split())
            print(f'Сумма вещественных параметров = {add(real)}')
        if var == 3:
            print('Arrivederci.')
            break
    except ValueError:
        print('Неверный формат чисел!')
    