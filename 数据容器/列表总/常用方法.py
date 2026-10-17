#.index(值)查找指定元素在列表中第一次出现的下标

# nums = [10, 20, 10, 40, 50]
# result=nums.index(10)
# print(result)




#.count(值)统计元素出现的次数

# nums = [10, 20, 10, 40, 50]
# result=nums.count(10)
# print(result)




#.reverse()反转列表  无返回值

# nums = [10, 20, 10, 40, 50]
# nums.reverse()
# print(nums)



#.sort(reverse=布尔值）对列表从小到大排序 无返回值
#reverse用于控制排列方式，输入为True即从大到小

#全是数字，则按大小排序
# nums=[23,11,32,30,17]
# nums.sort()
# print(nums)
#
# nums=[23,11,32,30,17]
# nums.sort(reverse=True)
# print(nums)


# 数字和字符串都有就会报错

# nums=[23,11,32,30,17,'魏依辰']
# nums.sort()
# print(nums)

#字符串按Unicode编码大小进行排序
# msg_list=['魏依辰','北京','工作']
# msg_list.sort()
# print(msg_list)
# print(ord('魏'),ord('北'),ord('工'))


#所有方法只在当前层面，不会深入到嵌套列表进行处理










