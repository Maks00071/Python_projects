def cezar_ru_encry(s: str, rot: int) -> str:
    '''Кодирует текст на русском языке'''
    encryption = ''
    for i in s:
        if i.isupper():
            if (ord(i) + rot) > 1071:
                encryption += chr((ord(i) + rot) - 32)
            else:
                encryption += chr(ord(i) + rot)
        elif i.islower():
            if (ord(i) + rot) > 1103:
                encryption += chr((ord(i) + rot) - 32)
            else:
                encryption += chr(ord(i) + rot)
        else:
            encryption += i
    return encryption


def cezar_en_encry(s: str, rot: int) -> str:
    '''Кодирует текст на английском языке'''
    encryption = ''
    for i in s:
        if i.isupper():
            if (ord(i) + rot) > 90:
                encryption += chr((ord(i) + rot) - 26)
            else:
                encryption += chr(ord(i) + rot)
        elif i.islower():
            if (ord(i) + rot) > 122:
                encryption += chr((ord(i) + rot) - 26)
            else:
                encryption += chr(ord(i) + rot)
        else:
            encryption += i
    return encryption


def cezar_ru_decry(s: str, rot: int) -> str:
    '''Дешифрует текст на русском языке'''
    decryption = ''
    for i in s:
        if i.isupper():
            if (ord(i) - rot) < 1040:
                decryption += chr((ord(i) - rot) + 32)
            else:
                decryption += chr(ord(i) - rot)
        elif i.islower():
            if (ord(i) - rot) < 1072:
                decryption += chr((ord(i) - rot) + 32)
            else:
                decryption += chr(ord(i) - rot)
        else:
            decryption += i
    return decryption


def cezar_en_decry(s: str, rot: int) -> str:
    '''Дешифрует текст на английском языке'''
    decryption = ''
    for i in s:
        if i.isupper():
            if (ord(i) - rot) < 65:
                decryption += chr((ord(i) - rot) + 26)
            else:
                decryption += chr(ord(i) - rot)
        elif i.islower():
            if (ord(i) - rot) < 97:
                decryption += chr((ord(i) - rot) + 26)
            else:
                decryption += chr(ord(i) - rot)
        else:
            decryption += i
    return decryption

def cezar_code():
    '''
    Функция кодирует / декодирует текст
    в зависимости от языка текста и сдвига
    '''
    string_in = input('Введите текст: ')
    print('Введите шаг кодировки')
    rot_in = int(input())
    language = input('Введите язык текста (en / ru: ')
    code = input('Введите, что надо сделать (enc = закодировать / dec = раскодировать)')
    if language == 'en':
        if code == 'enc':
            print(cezar_en_encry(string_in, rot_in))
        elif code == 'dec':
            print(cezar_en_decry(string_in, rot_in))
    elif language == 'ru':
        if code == 'enc':
            print(cezar_en_encry(string_in, rot_in))
        elif code == 'dec':
            print(cezar_en_decry(string_in, rot_in))

cezar_code()
