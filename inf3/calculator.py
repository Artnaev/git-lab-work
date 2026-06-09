# Изменено в ветке main
"""
Простой калькулятор
===================

Набор функций для выполнения базовых математических операций.

.. note:: Учебный проект для демонстрации документирования кода
.. seealso:: https://docs.python.org/3/library/math.html

.. todo:: Добавить логарифмы
.. todo:: Добавить тригонометрические функции
"""


def add(a, b):
    """
    Сложение двух чисел.
    
    :param a: первое число
    :param b: второе число
    :return: сумма a + b
    
    Пример:
    --------
    >>> add(5, 3)
    8
    """
    return a + b


def subtract(a, b):
    """
    Вычитание двух чисел.
    
    :param a: уменьшаемое
    :param b: вычитаемое
    :return: разность a - b
    
    Пример:
    --------
    >>> subtract(10, 4)
    6
    """
    return a - b


def multiply(a, b):
    """
    Умножение двух чисел.
    
    :param a: первый множитель
    :param b: второй множитель
    :return: произведение a * b
    
    Пример:
    --------
    >>> multiply(6, 7)
    42
    """
    return a * b


def divide(a, b):
    """
    Деление двух чисел.
    
    :param a: делимое
    :param b: делитель
    :return: частное a / b
    :raises ZeroDivisionError: если b равно нулю
    
    .. warning:: Деление на ноль невозможно!
    
    Пример:
    --------
    >>> divide(15, 3)
    5.0
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return a / b


def power(base, exponent):
    """
    Возведение числа в степень.
    
    :param base: основание
    :param exponent: показатель степени
    :return: base в степени exponent
    
    Пример:
    --------
    >>> power(2, 3)
    8
    >>> power(5, 2)
    25
    """
    return base ** exponent


# Демонстрация работы
if __name__ == "__main__":
    print("=" * 30)
    print("ПРОСТОЙ КАЛЬКУЛЯТОР")
    print("=" * 30)
    
    print("\nСложение:  5 + 3 =", add(5, 3))
    print("Вычитание: 10 - 4 =", subtract(10, 4))
    print("Умножение: 6 * 7 =", multiply(6, 7))
    print("Деление:   15 / 3 =", divide(15, 3))
    print("Степень:   2 ^ 10 =", power(2, 10))
    
    print("\nПроверка деления на ноль:")
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    
    print("\n" + "=" * 30)
