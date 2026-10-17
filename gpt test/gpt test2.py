students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 92},
    {"name": "小李", "score": 58},
    {"name": "小刚", "score": 55}
]

def find_excellent_student(students):
    excellent_student=[]
    for student in students:
        if student['score']>=90:
            excellent_student.append(student['name'])
    return excellent_student


def count_failed_students(students):
    count=0
    for student in students:
        if student['score']<60:
            count+=1
    return count

def calculate_passed_average(students):
    passed_nums=0
    passed_score=0
    for student in students:
        if student['score']>=60:
            passed_nums+=1
            passed_score+=student['score']
    passed_avg=passed_score/passed_nums
    return passed_nums, passed_avg

passed_count, passed_avg=calculate_passed_average(students)
failed_students=count_failed_students(students)
excellent_name=find_excellent_student(students)
print(f'优秀学生是{excellent_name}')
print(f'不及格人数有{failed_students}个')
print(f'及格人数为{passed_count}')
print(f'及格同学的平均分是{passed_avg:.1f}')