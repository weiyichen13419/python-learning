# def two_sum(nums:list[int],target:int) -> list[int]:
#     for num in nums:
#         if target - num in nums:
#             return [nums.index(num),nums.index(target-num)]
# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([3, 2, 4], 6))
# print(two_sum([3, 3], 6))
#
# def two_sum(nums:list[int],target:int) -> list[int]:
#     for i in range(len(nums)):
#         a=nums[i]
#         for j in range(i+1,len(nums)):
#             if a+nums[j]==target:
#                 return [i,j]

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        need = target - num
        if need in seen:
           return [seen[need], i]
        else:
            seen[num] = i

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([8, -2], 6) == [0, 1]

print("全部测试通过！")