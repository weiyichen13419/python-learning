# t1=(28,67,21,67,11)
# t2=('魏依辰','北京')
# t3=(100,True,'你好',None,(50,60,70))
# print(type(t1),t1)
# print(type(t2),t2)
# print(type(t3),t3)

# t1=(28,67,21,67,11)
# print(t1[1])
# print(t1[-2])

# 元组中内容不可更改，但嵌套的数组可以改
# t1=(28,67,21,67,11,[67,True,'你好',None,(50,60,70)])
# t1[5][1]=10
# print(t1)
# result=t1.count(67)
# print(result)
# 定义空元组
# t1 = ()
# t2 = tuple()

#一个元素元组的定义
# t1=('你好',)
# print(type(t1),t1)

# t1=(28,67,21,67,11)
# index=0
# while index < len(t1):
#     print(t1[index])
#     index+=1
#
t1=(28,67,21,67,11)
for item in t1:
    print(item)


