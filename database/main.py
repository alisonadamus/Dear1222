import sqlite3
# Підключення
conn = sqlite3.connect('company.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Створення таблиці
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        position TEXT,
        salary REAL
    )
''')

# Додавання даних
cursor.executemany('''
    INSERT OR IGNORE INTO employees (id, name, position, salary) 
    VALUES (?, ?, ?, ?)
''', [
    (1, 'Анна', 'Менеджер', 50000),
    (2, 'Петро', 'Розробник', 70000),
    (3, 'Іван', 'Дизайнер', 45000)
])

conn.commit()
# Запит
cursor.execute("SELECT name, salary, position FROM employees WHERE salary > 50000")
for row in cursor.fetchall():
    print(f"{row['name']} ({row['position']}): {row['salary']} грн")
# Закриття
conn.close()