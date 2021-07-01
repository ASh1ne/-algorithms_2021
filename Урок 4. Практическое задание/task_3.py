from timeit import timeit
import cProfile


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# была использована читерская функция реверс. Первое место не заняла, но 2 все-таки захватила.
def revers_4(enter_num):
    num_list = list(str(enter_num))
    num_list.reverse()
    revers_num = "".join(num_list)
    return revers_num


enter_num = int(input('Введите число: '))

revers_1(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)
revers_4(enter_num)

print(timeit(f'revers_1({enter_num})', globals=globals(), number=10000))
print(timeit(f'revers_2({enter_num})', globals=globals(), number=10000))
print(timeit(f'revers_3({enter_num})', globals=globals(), number=10000))
print(timeit(f'revers_4({enter_num})', globals=globals(), number=10000))

cProfile.run('revers_1(1000000)')
cProfile.run('revers_2(1000000)')
cProfile.run('revers_3(1000000)')
cProfile.run('revers_4(1000000)')

# Из представленных варинатов решения задачи самый быстрый - срез, поскольку он имеет
# самую простую сложность- O(n)
