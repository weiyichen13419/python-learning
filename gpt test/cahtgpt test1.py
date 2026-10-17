students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 92},
    {"name": "小李", "score": 88},
    {"name": "小刚", "score": 55}
]

def count_students(students):
    count = 0
    for stu in students:
        count+=1
    return count

def calc_avg(students):
    total = 0
    for stu in students:
        total+=stu['score']
    return total/len(students)

def find_best(students):
    top_student=students[0]
    for stu in students:
        if stu['score']>top_student['score']:
           top_student=stu
    return top_student

def find_passed_student(students):
    students_list=[]
    for stu in students:
        if stu['score']>=60:
           students_list.append(stu['name'])
    return students_list

def find_failed_student(students):
    students_list=[]
    for stu in students:
        if stu['score']<60:
            students_list.append(stu['name'])
    return students_list

passed_student=find_passed_student(students)
average=calc_avg(students)
top_student=find_best(students)
studentscount=count_students(students)
failed_student=find_failed_student(students)

print("学生人数：", studentscount)
print("班级平均分：", average)
print("最高分学生：", top_student)
print("最高分：", top_student['score'])
print("及格学生名单：", passed_student)
print(f'未及格学生有：{failed_student}')
