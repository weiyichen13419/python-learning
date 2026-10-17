# 查询
d1={'张三':72,'李四':60,'王五':85}
# 直接取值，若key不存在，报错
result = d1['张三']
print(result)
# 安全取值，若key不存在，返回默认值或者None
result=d1.get('古月方源','抱歉，key不存在')
print(result)

#新增
# d1={'张三':72,'李四':60,'王五':85}
# d1['赵六']=99
# print(d1)

#修改，直接新增，有重复会覆盖，无则加
#批量修改.update

#删除
d1={'张三':72,'李四':60,'王五':85}

#删除指定key对应的那组键值对
# del d1['张三']
# print(d1)

#.pop()删除指定key对应的那组键值对，并返回那个key所对应的值
# result=d1.pop('张三')
# print(d1)
# print(result)
#pop可以设置默认值，若想山粗的key不存在，会返回默认值而不报错
result=d1.pop('古月方源','删除失败！')
print(d1)
print(result)


