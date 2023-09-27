def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    result_nums1 = []
    result_nums2 = []
    result_with_two_array = []

    result_nums1 = set(nums1) - set(nums2)
    result_nums2 = set(nums2) - set(nums1)

    result_with_two_array.append(list(result_nums1))
    result_with_two_array.append(list(result_nums2))

    return result_with_two_array


nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

print(findDifference(nums1, nums2))
