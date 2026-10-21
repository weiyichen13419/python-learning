def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
#     numss1 = nums1.copy()
#     numss2 = nums2.copy()
#
#     if len(numss1) < len(numss2):
#         for num in numss1:
#             if num not in numss2:
#                 continue
#             else:
#                 result.append(num)
#                 numss2.remove(num)
#     else:
#         for num in numss2:
#             if num not in nums1:
#                 continue
#             else:
#                 result.append(num)
#                 numss1.remove(num)
#
#     return result
#
# assert sorted(intersect([1, 2, 2, 1], [2, 2])) == [2, 2]
# assert sorted(intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
# assert intersect([], [1, 2]) == []
# assert sorted(intersect([1, 1, 1], [1, 1])) == [1, 1]
# assert intersect([1, 2], [3, 4]) == []
# print("第一轮测试通过！")
    seen={}
    if nums1 ==[] or nums2 ==[]:
        return result

    for num in nums1:
        if num in seen:
            seen[num]+=1
        else:
            seen[num]=1

    for num in nums2:
        if seen.get(num,0) >0 :
            seen[num]-=1
            result.append(num)

    return result
#
# def intersect_min(nums1: list[int], nums2: list[int]) -> list[int]:
#     counts1 = {}
#     counts2 = {}
#     result = []
#
#     # 统计第一个列表
#     for num in nums1:
#         counts1[num] = counts1.get(num, 0) + 1
#
#     # 统计第二个列表
#     for num in nums2:
#         counts2[num] = counts2.get(num, 0) + 1
#
#     # 找出两个字典共同拥有的数字
#     for num in counts1:
#         if num in counts2:
#             times = min(counts1[num], counts2[num])
#             result.extend([num] * times)
#
#     return result
#

print(intersect_min([1, 2, 2, 1], [2, 2]))
print(intersect_min([1, 1, 1, 2], [1, 1, 3]))
assert sorted(intersect([1, 2, 2, 1], [2, 2])) == [2, 2]
assert sorted(intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
assert intersect([], [1, 2]) == []
assert sorted(intersect([1, 1, 1], [1, 1])) == [1, 1]
assert intersect([1, 2], [3, 4]) == []
print("第一轮测试通过！")