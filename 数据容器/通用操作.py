# list函数： 1.定义空列表；2.将【可迭代对象】转换为列表。
# res1=list(range(10))
# res2=list('古月方源')
# res3=list({10,20,30,40,50})
# res4=list({'张三':72,'李四':60,'王五':85})
# res5=list({'张三':72,'李四':60,'王五':85}.values())
# res6=list({'张三':72,'李四':60,'王五':85}.items())
# print(type(res1),res1)
# print(type(res2),res2)
# print(type(res3),res3)
# print(type(res4),res4)
# print(type(res5),res5)
# print(type(res6),res6)


# tuple函数：1.定义空元组；2.将【可迭代对象】转换为元组。
# res1=tuple(range(10))
# res2=tuple('古月方源')
# res3=tuple({10,20,30,40,50})
# res4=tuple({'张三':72,'李四':60,'王五':85})
# res5=tuple({'张三':72,'李四':60,'王五':85}.values())
# res6=tuple({'张三':72,'李四':60,'王五':85}.items())
# print(type(res1),res1)
# print(type(res2),res2)
# print(type(res3),res3)
# print(type(res4),res4)
# print(type(res5),res5)
# print(type(res6),res6)


# set函数： 1.定义空集合；2.将【可迭代对象】转换为集合。
# res1=set(range(10))
# res2=set('古月方源')
# res3=set({10,20,30,40,50})
# res4=set({'张三':72,'李四':60,'王五':85})
# res5=set({'张三':72,'李四':60,'王五':85}.values())
# res6=set({'张三':72,'李四':60,'王五':85}.items())
# print(type(res1),res1)
# print(type(res2),res2)
# print(type(res3),res3)
# print(type(res4),res4)
# print(type(res5),res5)
# print(type(res6),res6)


# str函数： 1.定义空字符串；2.将【任意类型】转换为字符串。
# res1=str(range(10))
# res2=str('古月方源')
# res3=str({10,20,30,40,50})
# res4=str({'张三':72,'李四':60,'王五':85})
# res5=str(False)
# res6=str(None)
# res7=str(100)
# print(type(res1),res1)
# print(type(res2),res2)
# print(type(res3),res3)
# print(type(res4),res4)
# print(type(res5),res5)
# print(type(res6),res6)
# print(type(res7),res7)


# dict函数： 1.定义空字典；2.将【可迭代对象】转换为字典。
#交给dict内容必须是键值对，不然会报错
res1=dict({'张三':72,'李四':60,'王五':85})
res2=dict([('张三',72),('李四',60),('王五',85)])
res3=dict((('张三',72),('李四',60),('王五',85)))
res4=dict({('张三',72),('李四',60),('王五',85)})
print(res1)
print(res2)

# 所有的数据容器，都支持【成员运算符】 in / not in 作用：判断某个元素是否在于容器中。
hobby=['看小说','打游戏','摄影']
nums=(10,20,30,40,50)
massage='hello world'
cities={'东京','大阪','京都'}
scores={'张三':72,'李四':60,'王五':85}

print('摄影' not in hobby)
print(80 not in nums)
print('hello' not in massage)
print('札幌' not in citys)
print('张三' not in scores)