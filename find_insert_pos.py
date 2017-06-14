#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You may assume no duplicates in the array.

# are few examples.
#[1,3,5,6], 5 → 2
#[1,3,5,6], 2 → 1
#[1,3,5,6], 7 → 4
#[1,3,5,6], 0 → 0

#Subscribe to see which companies asked this question.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        for i in range(1, len(nums)):
            if (target == nums[i]):
                return i
            elif nums[i - 1] < target <= nums[i]:
                return i
        return len(nums)
