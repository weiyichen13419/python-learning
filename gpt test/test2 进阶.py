students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 92},
    {"name": "小鬼", "score": 92},
    {"name": "小李", "score": 58},
    {"name": "小刚", "score": 55},
    {"name": "小华", "score": 76},
    {"name": "小丽", "score": 60}
]

def count_excllent_students(students):
    count = 0
    for student in students:
        if student['score']>=90:
            count += 1
    return count

def calculate_failed_average(students):
    failed_score = 0
    for student in students:
        if student['score']<60:
            failed_score += student['score']
    return failed_score/len(students)

def find_just_passed_students(students):
    passed_list = []
    for student in students:
        if student['score']==60:
            passed_list.append(student['name'])
    return passed_list

def find_top_students(students):
    # top_students=students[0]
    # for student in students:
    #     if student['score']>top_students['score']:
    #         top_students=student
    #     elif student['score']==top_students['score']:
    #         top_students.append(student)

    top_students = []
    best_score = 0
    for student in students:
        if student['score']>best_score:
            # top_students.clear()
            # top_students.append(student['name'])
            top_students = [student['name']]
            best_score = student['score']
        elif student['score']==best_score:
            top_students.append(student['name'])

    return top_students

def count_score_ranges(students):
    excellent_count = 0
    passed_count = 0
    failed_count = 0
    for student in students:
        if student['score']>=90:
            excellent_count += 1
        elif 60<=student['score']<90:
            passed_count += 1
        else:
            failed_count += 1

    return {
        'excellent_count': excellent_count,
        'passed_count': passed_count,
        'failed_count': failed_count
    }


count_all_students = count_excllent_students(students)
name_top_students = find_top_students(students)

print(f'优秀，及格，不及格的人数分别为{count_excllent_students(students)}')
print(f'最高分学生{name_top_students}')