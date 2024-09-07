def change_dec_number_sys(num: int, base: int) -> str:
    '''
    Функция переводит число с десятичной системой счисления
    в число с требуемой системой счисления

    num: число в десятичной системе счисления
    base: новая система счисления
    '''
    new_num = []
    while num >= base:
        rest = num % base
        num //= base
        new_num.append(str(rest))
    new_num.append(str(num))
    if base == 16:
        for ind, x in enumerate(new_num):
            if int(x) in range(10, 16):
                new_num[ind] = list('ABCDEF')[int(x) - 10]
        return ''.join(new_num[::-1])
    return ''.join(new_num[::-1])


def change_num_sys_in_dec(num: str, base: int) -> int:
    '''
    Функция переводит число с определенной системой счисления
    в число с десятичной системой счисления

    num: исходное число
    base: система счисления исходного числа
    '''
    array = list(num)[::-1]  # разбиваем число на разряды и переворачиваем список
    new_num = 0
    if base == 16:
        for i in range(len(array)):
            if array[i].isalpha():
                # берем индекс с списке и прибавляем 10, т.к. A, B, C, D, E, F - это 10, 11, 12, 13, 14, 15
                new_num += (list('ABCDEF').index(array[i]) + 10) * base ** i
            else:
                new_num += int(i) * base ** i
        return new_num
    else:
        for i in range(len(array)):
            new_num += int(array[i]) * base ** i
        return new_num


print('Ведите "dec", если необходимо перевести из десятичной системы счисления; "in dec", если в десятичную')
num_sys = input('Введите требуемое (dec / in dec): ')
if num_sys == 'dec':
    num = int(input('Введите исходное число: '))
    base = int(input('Введите новую систему счисления: '))
    print(change_dec_number_sys(num, base))
else:
    num = input('Введите исходное число: ')
    base = int(input('Введите исходную систему счисления: '))
    print(change_num_sys_in_dec(num, base))
