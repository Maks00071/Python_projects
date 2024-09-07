print('''Программа генерирует случайное число в диапазоне от 1 до 100 (включительно) и просит пользователя угадать это число.   
Если догадка меньше случайного числа, то программа выводит сообщение: "Слишком много, попробуйте еще раз".   
Если догадка меньше случайного числа, то программа выводит сообщение: "Слишком мало, попробуйте еще раз".   
Если пользователь угадал, то программа выводит сообщение: "Вы угадали, поздравляем!".

начинаем)))''')


import math
import random

def is_valid(elem: str):
    '''Функция проверяет корректность введенных данных
    True - если данные корректны: целое число от 1 до n включительно
    False - если данные не корректны
    '''
    if elem.isdigit():
        if 1 <= int(elem) <= 100:
            return True
        return False
    return False


def game_number():
    '''Основная программа игры'''
    secret_number = random.randint(1, 100)
    while True:
        guess_user = input('Введите ваше число: ')
        if is_valid(guess_user):
            if int(guess_user) == secret_number:
                print('Вы угадали, поздравляем!')
                break
            elif int(guess_user) > secret_number:
                print('Слишком много, попробуйте еще раз')
            elif int(guess_user) < secret_number:
                print('Слишком мало, попробуйте еще раз')
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
    print('Желаете еще раз сыграть?')
    game = input('Введите Да или Нет: ').lower()
    if game == 'да':
        game_number()
    else:
        print('Тогда до следующего раза!')
        return None
        
    
game_number()