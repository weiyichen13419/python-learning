#A .difference B
# s1={10,20,30,40,50}
# s2={30,40,50,60,70,}
# result=s1.difference(s2)
# print(s1)
# print(s2)
# print(result)
#A.difference_update B  删除A中B的元素
# s1={10,20,30,40,50}
# s2={30,40,50,60,70,}
# result=s1.difference_update(s2)
# print(s1)
# print(s2)
# print(result)

#A.union B
# s1={10,20,30,40,50}
# s2={30,40,50,60,70,}
# result=s1.union(s2)
# print(s1)
# print(s2)
# print(result)


#.issubset  A是不是B的子集 返回布尔值
# s1={10,20,30,40,50}
# s2={30,40,50,60,70,}
# s3={30,40,50}
# result=s3.issubset(s2)
# print(result)


#.issuperset  A是不是B的超集
# s1={10,20,30,40,50}
# s2={30,40,50,60,70,}
# s3={30,40,50}
# result=s1.issuperset(s3)
# print(result)
#.isdisjoint  看有没有交集,没有就True
s1={10,20,30,40,50}
s2={30,40,50,60,70,}
s3={30,40,50}
result=s3.isdisjoint(s2)
print(result)