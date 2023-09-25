# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    j = 0

    for i in range(0, len(nums)):
        if nums[i] != 0 and nums[j] == 0:
            nums[j], nums[i] = nums[i], nums[j]

        if nums[j] != 0:
            j += 1

    print(nums)


moveZeroes([0, 1, 0, 3, 12])
