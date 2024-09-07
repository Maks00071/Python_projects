def merge_sort(a: list, b: list) -> list:
    '''
    Сортирует по возрастанию два упорядоченных списка методом "Слияния"

    :param a: упорядоченный список
    :param b: упорядоченный список
    :return: отсортированный по возрастанию список
    '''

    c = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


def split_and_merge_list(a: list) -> list:
    '''
    Разделяет входной неупорядоченный список на прямом ходе рекурсии
    до состояния один элемент. Далее происходит слияние разделенного
    списка в единый упорядоченный по возрастанию список.

    :param a: Входящий неупорядоченный список
    :return: упорядоченный по возрастанию список
    '''

    n = len(a) // 2  # создаем точку деления списка
    first_half = a[:n]  # первая половина списка
    second_half = a[n:]  # вторая половина списка

    # если размер списка не один символ, то продолжаем его делить
    if len(first_half) > 1:
        first_half = split_and_merge_list(first_half)

    if len(second_half) > 1:
        second_half = split_and_merge_list(second_half)

    return merge_sort(first_half, second_half)  # начинаем постепенное слияние списков


a = list(map(int, input().split()))
a = split_and_merge_list(a)
print(a)