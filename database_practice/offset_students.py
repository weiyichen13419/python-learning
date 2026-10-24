
import sqlite3

conn = sqlite3.connect("practice.db")

try:
    result = conn.execute(
        "SELECT id,name FROM students ORDER BY id ASC LIMIT 1 OFFSET 1"
    )

    student = result.fetchone()

    print(student)

finally:
    conn.close()
