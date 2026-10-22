
import sqlite3

conn = sqlite3.connect("practice.db")

try:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS null_practice (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)

    conn.execute("DELETE FROM null_practice")

    conn.execute(
        "INSERT INTO null_practice (id, name) VALUES (?, ?)",
        (1, "张三")
    )

    conn.execute(
        "INSERT INTO null_practice (id, name) VALUES (?, ?)",
        (2, None)
    )

    conn.execute(
        "INSERT INTO null_practice (id, name) VALUES (?, ?)",
        (3, "李四")
    )

    conn.commit()

    result = conn.execute(
        "SELECT id, name FROM null_practice WHERE name IS NULL"
    )

    students = result.fetchall()

    print(students)

finally:
    conn.close()
