import random
import string

#  создадим строковые константы:
DIGITS = '0123456789'
LOWERCASE_LETTERS = string.ascii_lowercase
UPPERCASE_LETTERS = string.ascii_uppercase
PUNCTUATION = string.punctuation

chars = ''  #  будет содержать все символы, которые могут быть в генерируемом пароле

#  запрашиваум у пользователя следующую информацию:
cntPw = input('Укажите количество паролей для генерации:')
lenPw = input('Укажите длину одного пароля (не менее 8):')
digOn = input('Включать ли цифры 0123456789? (y/n)')
if digOn == 'y':
    chars += DIGITS
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
if ABCon == 'y':
    chars += UPPERCASE_LETTERS
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
if abcOn == 'y':
    chars += LOWERCASE_LETTERS
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
if chOn == 'y':
    chars += PUNCTUATION
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
if excOn == 'y':
    chars = ''.join([x for x in chars if x not in 'il1Lo0O'])

def generation_pass(lenght, chars):
    '''Функция генерирует безопасный пароль'''
    safe_pass = ''
    for i in range(int(lenght)):
        safe_pass += random.choice(chars)
    return safe_pass


for x in range(int(cntPw)):
    print(generation_pass(lenPw, chars))