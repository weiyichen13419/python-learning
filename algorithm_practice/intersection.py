def intersect_min(nums1: list[int], nums2: list[int]) -> list[int]:
    counts1 = {}
    counts2 = {}
    result = []

    # 统计第一个列表
    for num in nums1:
        counts1[num] = counts1.get(num, 0) + 1

    # 统计第二个列表
    for num in nums2:
        counts2[num] = counts2.get(num, 0) + 1

    # 找出两个字典共同拥有的数字
    for num in counts1:
        if num in counts2:
            times = min(counts1[num], counts2[num])
            result.extend([num] * times)

    return result

