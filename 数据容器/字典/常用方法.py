#keys方法，获取所有键  返回值为dict_keys
# d1={'张三':72,'李四':60,'王五':85}
# result=d1.keys()
# print(result)
# print(type(result))

# #dict_keys与列表类似可以被遍历，但不能通过下标访问元素

# for item in result:
#     print(item)

# l1=list(result)
# print(l1)
# print(type(l1))



#values方法，获取所有值
# d1={'张三':72,'李四':60,'王五':85}
# result=d1.values()
# print(result)
# print(type(result))


#items获得所有键值对
d1={'张三':72,'李四':60,'王五':85}
result=d1.items()
print(result)
print(type(result))
