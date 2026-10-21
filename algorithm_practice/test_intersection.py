from intersection import intersect_min


def test_basic():
    result = intersect_min([1, 2, 2, 1], [2, 2])
    assert sorted(result) == [2, 2]


def test_empty():
    result = intersect_min([], [1, 2])
    assert result == []


def test_no_common():
    result = intersect_min([1, 2], [3, 4])
    assert result == []

def test_negative():
    result = intersect_min([-3,-3,2],[-3,2,2])
    assert sorted(result) ==[-3,2]

def test_different_counts():
    result = intersect_min([5, 5, 5, 1] ,[5, 5, 1, 1, 1])
    assert sorted(result) == [1,5,5]

def test_swapped_inputs():
    nums1 = [1, 2, 2, 3]
    nums2 = [2, 2, 4]
    result=intersect_min(nums1, nums2)
    assert sorted(result) == [2,2]
    result=intersect_min(nums2, nums1)
    assert sorted(result) == [2, 2]