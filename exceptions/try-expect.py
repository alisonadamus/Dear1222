def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Помилка: ділення на нуль!")
        return None
    except TypeError:
        print("Помилка: введено некоректний тип даних!")
        return None
    else:
        print(f"Ділення успішне: {a} / {b} = {result}")
        return result
    finally:
        print("Завершення операції ділення.\n")


divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "2")