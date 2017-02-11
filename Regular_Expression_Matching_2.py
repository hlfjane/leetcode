"""Implement regular expression matching with support for '.' and '*'."""
"""'.' Matches any single character."""\
"""'*' Matches zero or more of the preceding element."""
"""Using dynamic programming, as the overall result can be treated as the problem solution result"""
"""setup 2 dimention arrary, dp[m+1][n+1] where dp[0][0] is True, m is the len(s), n is len(p)"""
"""dp[0][0] means s, p are both empty"""
"""dp[i][j] means s[0,i) matches p[0,j)"""
"""the algorithm of this dp is describe as below"""
"""dp[i][j] = dp[i-1][j-1], when p[j-1] != '*' and (s[i-1] == p[j-1] or p[j-1] == '.')"""
"""dp[i][j] = dp[i][j-2] when p[j-1] == '*' and dp[i][j-2] == True"""
"""dp[i][j] = dp[i][j-1] when i > 0 and (s[i-1]==p[j-2] || p[j-2]=='.')"""
class Solution(object):
    def __init__(self):
        pass
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp=[([False]*(n + 1)) for i in range(m + 1)]

        dp[0][0] = True
        print dp, m, n
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    print "in *"
                    dp[i][j] = dp[i][j-2] or (i > 0 and dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j] = i > 0 and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                print i,j,dp[i][j]
        return dp[m][n]

def main():
    S = Solution()
    result = S.isMatch("aa",'aa')
    print result
main()
    
