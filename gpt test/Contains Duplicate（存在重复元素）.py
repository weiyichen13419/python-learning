def contains_duplicate(nums:list[int]) -> bool:
    # 集合方法
    # s=set(nums)
    # if len(s) == len(nums):
    #     return False
    # else:
    #     return True

    # s=set()
    # for i in nums:
    #     if i in s:
    #         return True
    #     else:
    #         s.add(i)
    #
    # return False


    # if len(s) == len(nums):
    #     return False
    # else:
    #     return True

    seen={}
    for num in nums:
        if num in seen:
            return True
        seen[num]=1
    return False


assert contains_duplicate([1, 2, 3, 1]) is True
assert contains_duplicate([1, 2, 3, 4]) is False
assert contains_duplicate([1, 1, 1, 3]) is True
assert contains_duplicate([]) is False
assert contains_duplicate([-1, 2, -1]) is True
assert contains_duplicate([0]) is False

print("6组测试全部通过！")