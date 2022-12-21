
# Задание 1

def password_validate(passwd: str) -> bool:
    """Функция проверки пароля на соответствие требованиям

    args: 
        passwd - пароль в виде строки
    returns:
        True - пароль проходит по требованиям
        False - пароль не проходит по требованиям
    """

    if len(passwd) < 6:
        return False
    if 'password' in passwd.lower():
        return False
    count_digit = 0
    for i in passwd:
        if i.isdigit():
            count_digit += 1
    if count_digit >= 1 and count_digit != len(passwd):
        return True
    else:
        return False


user_input = input('Введите пароль на проверку: ')

if password_validate(user_input):
    print(f'Пароль подходит, функция вернула {True}')
else:
    print(f'Пароль не подходит, функция вернула {False}')
