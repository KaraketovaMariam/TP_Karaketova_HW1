import pytest
from ..main import calculate


# Тест для проверки на то, что возникает исключение ValueError, если в файле находятся некорректные данные
def test_broken_file():
    numbers = [9, 46, -33, 'x', -44, 'mistake', 98, -97, -37, -23]
    line = ' '.join(str(number) for number in numbers)
    with open('input.txt', 'w') as file:
        file.write(line)
    with pytest.raises(ValueError):
        calculate()
