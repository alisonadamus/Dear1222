import doctest


def add(a, b):
    """
    Повертає суму двох чисел.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b


def is_even(n):
    """
    Перевіряє, чи є число парним.

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    """
    return n % 2 == 0


def greet(name):
    """
    Повертає привітання.

    >>> greet("Аліса")
    'Привіт, Аліса!'
    >>> greet("Богдан")
    'Привіт, Богдан!'
    """
    return f"Привіт, {name}!"


def square(x):
    """
    Повертає квадрат числа.

    >>> square(2)
    4
    >>> square(-3)
    9
    """
    return x ** 2


doctest.testmod()
