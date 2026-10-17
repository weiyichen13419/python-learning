score_list = [62, 50, 60, 48, 80, 20, 95]
score_list.sort(reverse=True)
# index=0
# while index<len(score_list):
#     print(score_list[index])
#     index+=1

# 写法1
# for item in score_list:
#     print(item)
# 2
# for index in range(len(score_list)):
#     print(score_list[index])
# 3 enumerate中的start参数，可以让计数从指定值开始（改变的是循环时的编号而不是真正的索引值）
for index, item in enumerate(score_list):
    print(index, item)
