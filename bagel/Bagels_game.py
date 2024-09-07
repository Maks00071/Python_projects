import random

NUM_DIGITS = 3  # кол-во цифр в секретном числе
MAX_GUESSES = 10  # кол-во максимальных попыток


def main():
    print('''Bagels, a deductive logic game. 
          By Al Sweigart al@inventwithpython.com

          I am thinking of a {}-digit number with no repeated digits.
          Try to guess what it is. Here ara some clues:
          When I say:    That means:
          Pico           One digit is correct but in the wrong position.
                         (Одна цифра правильная, но стоит в неправильной позиции)   
                         
          Fermi          One digit is correct and in the right position.
                         (Одна цифра правильная и стоит на своем месте)   
            
          Bagels         No digit is correct.
                         (Правильных цифр нет)

        For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.''')

    while True:  # основной цикл игры
        secretNum = getSecretNum()  # Переменная, в которой хранится секретное число, которое должен угадать игрок
        print('I have thought up a number.')  # "Я загадал число."
        print(f'You have {MAX_GUESSES} guesses to get it.')  # "У тебя есть ... кол-во попыток."

        numGuesses = 1  # первая попытка
        while numGuesses <= MAX_GUESSES:  # пока не закончатся попытки
            guess = ''
            # продолжаем итерации до получения правильной догадки
            while len(guess) != NUM_DIGITS or not guess.isdecimal():  # isdecimal() - все ли символы строки десятичные только цифры)
                print(f'Guess №{numGuesses}: ')
                guess = input('> ')

            clues = getClues(guess, secretNum)  # получаем информацию из функции
            print(clues)
            numGuesses += 1  # увеличиваем число попыток

            if guess == secretNum:
                break  # мы угадали число
            if numGuesses > MAX_GUESSES:  # кол-во попыток превышает максимально допустимое
                print('You ran out of guesses.')  # "У тебя закончились попытки"
                print(f'The answer was {secretNum}.')  # Правильное число ...

        print('Do you want to play again? (yes or no)')  # Спрашиваем игрока, хочет ли он сыграть снова
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    '''Возвращает строку из NUM_DIGITS уникальных случайных цифр.'''
    numbers = list('0123456789')  # создаем список цифр от 0 до 9
    random.shuffle(numbers)  # shuffle перемешивает цифры в случайном порядке

    # Берем первые NUM_DIGITS цифр списка для нашего секретного числа
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    '''Возвращает строку с подсказками pico, fermi и bagels для полученной
    на входе пары из догадки и секретного числа.'''
    if guess == secretNum:
        return 'You got it!'  # "У тебя получилось!"

    clues = []  # если номера не совпали, создаем пустой список

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:  # правильная цифра на правильном месте
            clues.append('Fermi')
        elif guess[i] in secretNum:  # правильная цифра на неправильном месте
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # правильных цифр нет вообще
    else:
        clues.sort()  # сортируем подсказки в алфавитном порядке, чтобы их исходный порядок ничего не выдавал
        return ' '.join(clues)  # склеиваем список подсказок в одно строковое значение


if __name__ == '__main__':  # если программа не импортируется, а запускается, производим запуск
    main()
