"""Median of Two Sorted Arrays """
"""There are two sorted arrays nums1 and nums2 of size m and n respectively."""
"""Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n))."""
class Solution(object):
    def __init__(self):
        pass
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_list = nums1 + nums2
        new_list.sort()
        total_len = len(new_list)
        target = 0
        if total_len ==0:
            return target
        if total_len%2 == 0:
            target = (new_list[total_len/2 - 1]+new_list[total_len/2])/2 + 0.5*((new_list[total_len/2 - 1]+new_list[total_len/2])%2)
        else:
            target = new_list[total_len/2]
        return target

def main():
    l1 = [1,5,9,12,15,19,28]
    l2 = [5,6,7,9,18,21,230,234]
    S = Solution()
    target = S.findMedianSortedArrays(l1,l2)
    print target

main()
