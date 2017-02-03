"""Palindrome Number"""
"""Determine whether an integer is a palindrome. Do this without extra space."""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            digit_num = 1
            while x/pow(10,digit_num) != 0:
                digit_num += 1
            for i in range(digit_num/2):
                if (x/(pow(10,digit_num - 1 - i)))%10 != x%10:
                    return False
                else:
                    x = x/10
                    digit_num -= 1
        return True

def main():
    s = Solution()
    num = 10001
    result = s.isPalindrome(num)
    if result == True:
        print ("Yes")
    else:
        print ("No")
main()
