# msg='welcome to japan'
# print(msg[3])
#字符串中字符不可修改
#字符串不能嵌套
# msg='welcome to japan'
# result=msg.index('a')
# print(result)

# msg='welcome@to@japan'
# # result=msg.split('@')
# # print(result)
# result=msg.replace('a','A')
# print(result)

# msg='welcome to japan'
# result = msg.count('a')
# print(result)

# strip 方法：从某个字符串中删除：指定字符串中的任意字符
# 规则：从字符串两端开始删除，直到遇到第一个不在字符串中的字符就停下
msg='666we6l6c6ome t6o ja6pa6n6666'
result = msg.strip('6')
print(msg)
print(result)
