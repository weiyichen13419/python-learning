
import sqlite3

conn = sqlite3.connect("practice.db")


    # result = conn.execute(
    #     "SELECT id, name FROM students ORDER BY id"
    # )

    # students = result.fetchall()

    # student_list = []
    # for student in students:
    #     student_info = {
    #         "id": student[0],
    #         "name": student[1]
    #     }
    #     student_list.append(student_info)
    # print(student_list)
        # print(student_info['name'])
def student_exists(student_id):
    try:
        result = conn.execute("SELECT COUNT(*) FROM students WHERE id=?",(student_id,))
        row=result.fetchone()
        exists=row[0]>0
        return exists

    finally:
        conn.close()
print(student_exists(1))

