
import sqlite3

conn = sqlite3.connect("practice.db")

try:
    result = conn.execute(
        "SELECT id,name FROM students ORDER BY id DESC"
    )

    students = result.fetchall()

    print(students)

finally:
    conn.close()
