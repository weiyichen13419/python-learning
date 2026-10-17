# #set/frozenset 不重复，无序
# s1={10,20,30,40,50,10,10,10,60,100}
# s2={'cuc','工作','python','北京','魏依辰','你好','你好'}
# s3={10,'你好',1,True,12.4}
# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)

# s1=frozenset({10,20,30,40,50,10,10,10,60,100})
# s2=frozenset({'cuc','工作','python','北京','魏依辰','你好','你好'})
# s3=frozenset({10,'你好',1,True,12.4})
# print(s1)
# # s2.add('hhh')
# print(s2)
# print(s3)

# s1=frozenset([10,20,30,40,50])
# s2=frozenset((10,20,30,40,50))
# s3=frozenset('hello world')
# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)

# # 空集合,可变
# s1 = set()
# print(s1)
# #不可变空集合
# s2=frozenset()
# print(type(s2))
# print(s2)
# #空字典
# s3={}
# print(type(s3),s3)


#集合不能嵌套可变集合
s1={10,20,30,40,50}
s2=frozenset({10,20,30,40,50})
l1=[1,2,3,4,5]
t1=('hello','world')

s3={'魏依辰','北京',t1}
print(s3)

