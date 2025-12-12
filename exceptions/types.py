try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Помилка: {e} — не можна ділити на нуль!")

try:
    number = int("abc")
except ValueError as e:
    print(f"Помилка: {e} — не вдалося перетворити текст у число!")

try:
    result = "5" + 3
except TypeError as e:
    print(f"Помилка: {e} — не можна додавати рядок і число!")

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print(f"Помилка: {e} — індекс поза межами списку!")

my_dict = {"name": "Олег", "age": 25}
try:
    print(my_dict["city"])
except KeyError as e:
    print(f"Помилка: ключ {e} не існує в словнику!")

try:
    with open("немає_такого_файлу.txt") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Помилка: {e} — файл не знайдено!")

text = "привіт"


try:
    text.append("!")
except AttributeError as e:
    print(f"Помилка: {e} — рядок не має методу append!")

try:
    import nonexistent_module
except ImportError as e:
    print(f"Помилка: {e} — модуль не знайдено!")

try:
    print(abcd())
except NameError as e:
    print(f"Помилка: {e} — назву не знайдено!")

try:
    print(abc)
except Exception as e:
    print(f"Помилка: {type(e).__name__} - {e}")