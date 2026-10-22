import sqlite3
conn = sqlite3.connect("practice.db")
# conn.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY,name TEXT)")
# result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
# print(result.fetchone())
# conn.execute("INSERT INTO students(id,name) VALUES(1,'张三')")
# conn.commit()
# result = conn.execute("SELECT id, name FROM students ORDER BY id")
# print(result.fetchall())
# conn.execute("INSERT INTO students(id,name) VALUES(2,'李四')")
# conn.commit()
# result = conn.execute("SELECT id,name FROM students")
# print(result.fetchall())

# target_id=1
# result=conn.execute("SELECT id,name FROM students WHERE id=?",(target_id,))
# print(result.fetchone())

# student_id = 3
# student_name = "王五"

# conn.execute(
#     "INSERT INTO students(id,name) VALUES (?,?)",
#     (student_id,student_name)
# )
# conn.commit()
# result=conn.execute("SELECT id,name FROM students ORDER BY id")
# print(result.fetchall())

def get_student(student_id):
    result = conn.execute(
        "SELECT id, name FROM students WHERE id = ?",
        (student_id,)
    )
    return result.fetchone()

try:
    user_input = input("请输入学生编号：")
    student_id = int(user_input)

    student = get_student(student_id)

    if student is None:
        print("没有找到这个学生")
    else:
        print(student)

except ValueError:
    print("输入错误：学生编号必须是整数")
finally:
    conn.close()
    print("数据库连接已关闭")