fruits={
    '苹果':4.5,
    '香蕉':3.2,
    '橙子':5.8,
    '草莓':12.0,
    '哈密瓜':8.8
}
for key in fruits:
    print(f'{key}:{fruits[key]}')
print(fruits.get('苹果'))
result=max(fruits,key=fruits.get)
print(f'最贵的的水果是{result}，它的价格是{fruits[result]}')

# 练习二: 学生成绩表
# students = [
#     {
#         'name': '张三',
#         'scores': {'语文': 88, '数学': 92, '英语': 95}
#     },
#     {
#         'name': '李四',
#         'scores': {'语文': 75, '数学': 83, '英语': 80}
#     },
#     {
#         'name': '王五',
#         'scores': {'语文': 92, '数学': 95, '英语': 88}
#     }
# ]
#
# #最高分
# # for stu in students:
# #     scores_list=stu['scores'].values()
# #     avg=sum(scores_list)/len(scores_list)
# #     print(f'scores_list:{scores_list}')
# #     print(f'avg:{avg:.1f}')
#
# # def find_best():
# #     best_score=0
# #     for stu  in students:
# #         res=sum(stu['scores'].values())
# #         if res>best_score:
# #             best_students = [stu['name']]
# #             best_score=res
# #         elif res==best_score:
# #             best_students.append(stu['name'])
# #
# #     print(f'{best_score}')
# # find_best()
#
# comment='这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝！强烈推荐！'
#
# print(comment.count('好喝'))
#
# comment2=comment.replace('贵','略高')
# print(comment2)
#
# print('好喝'in comment)
