
import sqlite3

conn = sqlite3.connect("practice.db")

try:
    # 任务1：查询按 id 升序排列的前两条学生记录
    result = conn.execute(
        "SELECT id,name FROM students ORDER BY id ASC LIMIT 2"
    )

    # 任务2：获取查询结果中的所有记录
    students = result.fetchall()

    print(students)

finally:
    conn.close()
