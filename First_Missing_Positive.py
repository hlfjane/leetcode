"""Given an unsorted integer array, find the first missing positive integer. """
"""Given [1,2,0] return 3"""
"""Given [3,4,-1,1] return 2."""
"""Given [3,4,5,1,8,2] return 6."""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_missing_positive = 1
        length = len(nums)
        for i in range(length):
            while nums[i] != 0:
                if nums[i] > length or nums[i] < 0 :
                    nums[i] = 0
                else:
                    if nums[i] == nums[(nums[i]-1)]:
                        break
                    tmp = nums[(nums[i]-1)]
                    nums[(nums[i]-1)] = nums[i]
                    nums[i] = tmp

        for i in range(length):
            if nums[i] != i + 1:
                first_missing_positive = i + 1
                break
            else:
                first_missing_positive = nums[i] + 1
        return first_non_positive
