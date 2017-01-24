"""Given an array of integers, return indices of the two numbers such that they"""
"""add up to a specific target"""
"""Assume that each input would have exactly one solution"""
class Solution(object):
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        length = len(nums)
        if length == 1 and nums[0] != target:
            return None
        for i in range(0, length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
