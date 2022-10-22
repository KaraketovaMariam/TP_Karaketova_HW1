import random
from time import time
from ..main import calculate, _min, _max, _sum, _mult


input_file = 'input.txt'
max_number = 1000001
step = 100000


# Генерирует набор тестовых случайных чисел
def random_nums(count = 10):
    numbers = [random.randint(-100, 100) for _ in range(count)]
    return numbers


# Проверяет время работы функции calculate
def test_time_calculate():
    report_file = 'tests/calculate.csv'
    with open(report_file, 'w') as file:
        file.write(f'"numbers","elapsed seconds"\n')
    for count in range(1, max_number, step):
        numbers = random_nums(count)
        line = " ".join(str(number) for number in numbers)
        with open(input_file, 'w') as file:
                file.write(line)
        t0 = time()
        calculate()
        t1 = time()
        elapsed = t1 - t0
        with open(report_file, 'a') as file:
            file.write(f'{count},{elapsed}\n')
        assert elapsed < 1


# Проверяет время работы функции _min
def test_time_min():
    report_file = 'tests/min.csv'
    with open(report_file, 'w') as file:
        file.write(f'"numbers","elapsed seconds"\n')
    for count in range(1, max_number, step):
        numbers = random_nums(count)
        t0 = time()
        _min(numbers)
        t1 = time()
        elapsed = t1 - t0
        with open(report_file, 'a') as file:
            file.write(f'{count},{elapsed}\n')
        assert elapsed < 0.1


# Проверяет время работы функции _max
def test_time_max():
    report_file = 'tests/max.csv'
    with open(report_file, 'w') as file:
        file.write(f'"numbers","elapsed seconds"\n')
    for count in range(1, max_number, step):
        numbers = random_nums(count)
        t0 = time()
        _max(numbers)
        t1 = time()
        elapsed = t1 - t0
        with open(report_file, 'a') as file:
            file.write(f'{count},{elapsed}\n')
        assert elapsed < 0.1


# Проверяет время работы функции _sum
def test_time_sum():
    report_file = 'tests/sum.csv'
    with open(report_file, 'w') as file:
        file.write(f'"numbers","elapsed seconds"\n')
    for count in range(1, max_number, step):
        numbers = random_nums(count)
        t0 = time()
        _sum(numbers)
        t1 = time()
        elapsed = t1 - t0
        with open(report_file, 'a') as file:
            file.write(f'{count},{elapsed}\n')
        assert elapsed < 0.1


# Проверяет время работы функции _mult
def test_time_mult():
    report_file = 'tests/mult.csv'
    with open(report_file, 'w') as file:
        file.write(f'"numbers","elapsed seconds"\n')
    for count in range(1, max_number, step):
        numbers = random_nums(count)
        t0 = time()
        _mult(numbers)
        t1 = time()
        elapsed = t1 - t0
        with open(report_file, 'a') as file:
            file.write(f'{count},{elapsed}\n')
        assert elapsed < 0.1