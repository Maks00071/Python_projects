import time

def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"time = {dt} sec")
        return result
    return wrapper

@test_time
def get_nod_slow(x, y):
    '''
    Вычисляется НОД для натуральных чисел x и y по медленному алгоритму Евклида

    :param x: первое натуральное число
    :param y: второе натуральное число
    :return: НОД
    '''
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

@test_time
def get_nod_fast(x, y):
    '''
    Вычисляется НОД для натуральных чисел x и y по быстрому алгоритму Евклида

    :param x: первое натуральное число
    :param y: второе натуральное число
    :return: НОД
    '''
    if x < y:
        x, y = y, x

    while y != 0:
        x, y = y, x % y
    return x

res1 = get_nod_fast(2, 100_000_000)
res2 = get_nod_slow(2, 100_000_000)
print(res1, res2)