# Читает числа из файла, считает нужные значения и выводит результат
def calculate():
    numbers = _read_nums('input.txt')
    print(f'В файле: {" ".join(str(number) for number in numbers)}')
    print(f'Минимальное: {_min(numbers)}')
    print(f'Максимальное: {_max(numbers)}')
    print(f'Сумма: {_sum(numbers)}')
    print(f'Произведение: {_mult(numbers)}')


# Функция чтения из файла
def _read_nums(file_name):
    with open(file_name) as file:
        first_line = file.readline()
    numbers = [int(number) for number in first_line.split()]
    return numbers


# Функция поиска минимума
def _min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number


# Функция поиска максимума
def _max(numbers):
    max_number = numbers[0]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    return max_number


# Функция поиска суммы
def _sum(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number
    return sum_numbers


# Функция поиска произведения
def _mult(numbers):
    mult_numbers = 1
    for number in numbers:
        mult_numbers *= number
    return mult_numbers


if __name__ == '__main__':
    calculate()