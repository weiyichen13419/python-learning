
import sqlite3

conn = sqlite3.connect("practice.db")

try:
    new_name = "王五同学"
    target_id = 3

    cursor = conn.execute(
        "UPDATE students SET name=? WHERE id=?",
        (new_name, target_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        print("修改失败：没有找到这个学生")
    else:
        print("修改成功")

finally:
    conn.close()
