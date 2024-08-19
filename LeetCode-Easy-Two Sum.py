"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indx_lst = []
    counter = 0
    for i in nums:
        if target-i in nums[counter+1:]:
            other = target-i
            indx_lst.append(counter)
            indx_lst.append(nums.index(other, counter+1))
        counter += 1
    print(indx_lst)


# Examples Tested
twoSum([2, 7, 11, 15], 9)
twoSum([3, 2, 4], 6)
twoSum([3, 3], 6)
