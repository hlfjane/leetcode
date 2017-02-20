"""Given a set of candidate numbers (C) (without duplicates) and a target number (T)"""
"""find all unique combinations in C where the candidate numbers sums to T"""
"""The same repeated number may be chosen from C unlimited number of times"""
"""All numbers (including target) will be positive integers."""
"""The solution set must not contain duplicate combinations."""
"""For example, given candidate set [2, 3, 6, 7] and target 7, """
"""solution is [[7],[2,2,3]]"""
"""dynamic programming"""
"""i means target_set 1-target"""
"""attention: the ',' used in dp[i] += (pre_list + [num],), very special"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [[[]]] + [[] for i in xrange(target)]
        for i in xrange(1, target+1):
            for num in candidates:
                if num>i: break
                for pre_list in dp[i - num]:
                    if not pre_list or num >= pre_list[-1]: 
                        dp[i] += (pre_list + [num],)
                #print dp[i]
        return dp[target]
