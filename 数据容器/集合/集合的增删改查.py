# # .add(元素)
# # .update(元素)必须传递可迭代对象
# # s1={10,20,30,40,50}
# # s1.add(60)
# # print(s1)
#
# # s1={10,20,30,40,50}
# # s1.update([60,70])
# # s1.update((80,90))
# # s1.update({100,200})
# # s1.update(range(0,5))
# # print(s1)
#
#
#
# #删
# # .remove如果指定元素不存在会报错
# s1={10,20,30,40,50}
# s1.remove(10)
# print(s1)

# # .discard不报错
# s1={10,20,30,40,50}
# s1.remove(10)
# print(s1)

# # .pop,会返回删除的随机值
# s1={10,20,30,40,50}
# result=s1.pop()
# print(s1)
# print(result)

# # .clear清空
# s1={10,20,30,40,50}
# s1.clear()
# print(s1)


#改不了，因为无下标也不支持replace，可以用remove+add
s1={10,20,30,40,50}
s1.remove(10)
s1.add(66)
print(s1)

#查不了，不具备按位访问能力
