
import sqlite3

conn = sqlite3.connect("practice.db")

def delete_student(student_id):
    cursor = conn.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )
    conn.commit()
    count = cursor.rowcount
    if count > 0:
        return True
    else:
        return False



try:
    result = delete_student(99)
    if result:
        print("学生删除成功")
    else:
        print("删除失败：学生不存在")

finally:
    conn.close()
