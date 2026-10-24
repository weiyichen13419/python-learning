
import sqlite3
import json

conn = sqlite3.connect("practice.db")

try:
    result = conn.execute(
        "SELECT id, name FROM students ORDER BY id ASC"
    )

    students = result.fetchall()

    student_list = []

    for student in students:
        student_info = {
            "id": student[0],
            "name": student[1]
        }

        student_list.append(student_info)

    # 第37课：请独立补全这里
    json_text = json.dumps(student_list,ensure_ascii=False)

    print(json_text)
    print(type(json_text))

finally:
    conn.close()
