# 观察 % 的位置
# '张%'	以“张”开头
# '%张'	以“张”结尾
# '%张%'	包含“张”


import sqlite3

conn = sqlite3.connect("practice.db")

try:
    keyword = "张"

    result = conn.execute(
        "SELECT id,name FROM students WHERE name LIKE ?",("%"+keyword+"%",)

    )

    students = result.fetchall()

    print(students)

finally:
    conn.close()
