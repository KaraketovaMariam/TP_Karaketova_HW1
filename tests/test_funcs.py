import random
import math
from ..main import _min, _max, _sum, _mult


# Генерирует набор тестовых случайных чисел
def random_nums(count = 10):
    numbers = [random.randint(-100, 100) for _ in range(count)]
    return numbers


# Проверяет работу функции поиска минимума, сравнивая результат со встроенной функцией
def test_min():
    numbers = random_nums()
    assert min(numbers) == _min(numbers)


# Проверяет работу функции поиска максимума, сравнивая результат со встроенной функцией
def test_max():
    numbers = random_nums()
    assert max(numbers) == _max(numbers)


# Проверяет работу функции поиска суммы, сравнивая результат со встроенной функцией
def test_sum():
    numbers = random_nums()
    assert sum(numbers) == _sum(numbers)


# Проверяет работу функции поиска произведения, сравнивая результат со встроенной функцией
def test_mult():
    numbers = random_nums()
    assert math.prod(numbers) == _mult(numbers)
