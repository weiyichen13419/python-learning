
import sqlite3

conn = sqlite3.connect("practice.db")

try:
    keyword = "李"

    result = conn.execute(
        "SELECT id,name FROM students WHERE id=1 OR name LIKE ?",
        (keyword + "%",)
    )

    students = result.fetchall()

    print(students)

finally:
    conn.close()
