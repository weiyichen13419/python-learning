# fruits={
#     '月光蛊':1,
#     '小光蛊':2,
#     '血源蛊':3
# }
# print(fruits.keys())
# max=max(fruits,key=fruits.get)
# print(max)

# 练习二: 学生成绩表
students = [
    {
        'name': '张三',
        'scores': {'语文': 88, '数学': 92, '英语': 95}
    },
    {
        'name': '李四',
        'scores': {'语文': 75, '数学': 83, '英语': 80}
    },
    {
        'name': '王五',
        'scores': {'语文': 92, '数学': 95, '英语': 88}
    }
]

def best_find():
    best_students=[]
    best_score=0
    for stu in students:
        total_score=sum(stu['scores'].values())

        if total_score>best_score:
            best_students=[stu['name']]
            best_score=total_score
        elif total_score==best_score:
            best_students.append(stu['name'])
    print(f'最高分是{best_score},获得了最高分的学生有{best_students}')
best_find()