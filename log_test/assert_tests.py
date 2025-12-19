def divide(a, b):
    assert b != 0, "Ділення на нуль заборонено!"
    return a / b

print(divide(10, 2))
print(divide(10, 0))


def add(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), \
        "Аргументи повинні бути числами!"
    return a + b

print(add(2, 3))
print(add("2", 3))


numbers = [1, 2, 3, -4, -5]
for n in numbers:
    assert n > 0, f"Число {n} не є додатним!"

print("Усі числа додатні")
# a = 5
# b = 10
# assert a + b == 15, "Is okey"
# assert a - b == 0, "Is not okey"