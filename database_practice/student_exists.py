
import sqlite3

conn = sqlite3.connect("practice.db")

def student_exists(student_id):
        result = conn.execute("SELECT COUNT(*) FROM students WHERE id=?",(student_id,))
        row=result.fetchone()
        exists=row[0]>0
        return exists


try:

    print(student_exists(2))

    print(student_exists(99))


finally:

    conn.close()