from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


# выбрал самое неудачное решение, потому что сортировка это O(n log N)
def func_3(array):
    my_count = list(({i: array.count(i) for i in array}).items())
    my_count.sort(key=lambda i: i[1])
    return f'Число {my_count[-1][0]} встречается больше всего раз: {my_count[-1][1]}'


print(timeit(f'func_1({array})', globals=globals(), number=10000))
print(timeit(f'func_2({array})', globals=globals(), number=10000))
print(timeit(f'func_3({array})', globals=globals(), number=10000))
