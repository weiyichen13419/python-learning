#不能用while
# d1={'张三':72,'李四':60,'王五':85}
# for key in d1:
#     print(f'{key}的成绩是: {d1[key]}')

d1 = {'张三': 72, '李四': 60, '王五': 85}
for key in d1.keys():
    print(f'{key}的成绩是: {d1[key]}')

