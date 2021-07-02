import timeit
from timeit import Timer

nums = [el for el in range(10000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Оптимизацию функции провел через LC, т.к. такой способ работает быстрее при O(n)
def func_2(nums):
    ind = [i for i in range(1, len(nums)) if nums[i] % 2 == 0]
    return ind


print('Дефолтная функция', timeit.timeit("func_1(nums)", globals=globals(), number=1000))
print('Доработанная функция', timeit.timeit("func_2(nums)", globals=globals(), number=1000))

# Дефолтная функция 2.0441576
# Доработанная функция 1.7283583
