class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp=[([False]*(n + 1)) for i in range(m + 1)]
        dp[0][0] = True
        for i in range( m + 1 ):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    dp[i][j] = (i>0 and dp[i-1][j]) or ( j > 0 and dp[i][j-1] )
                else:
                    dp[i][j] = i > 0 and dp[i-1][j-1]  and (p[j-1] == s[i-1] or p[j-1]=='?')
        return dp[m][n]
def main():
    S = Solution()
    result = S.isMatch("hello","*o*")
    print result

main()
