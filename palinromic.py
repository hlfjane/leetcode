"""Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000."""
"""Input: "babad" Output: "bab", Note: "aba" is also a valid answer."""
"""Input: "cbbd" , output: "bb" """
"""Note odd or even issue"""
"""extend the string as "#a#b#a#b#a" """
class Solution(object):
    def __init__(self):
        self.start = 0
        self.stop = 0

    def is_palindromic(self,center, s):
        if center >= len(s)/2:
            stop = len(s) - center
        else:
            stop = center + 1
        leng = 1
        palinromic = s[center]
        for i in range(1, stop):
            if s[center - i] == s[center + i]:
                leng += 2
                palinromic = s[center-i : center + i + 1]
                self.start = center-i
                self.stop = center + i
            else:
                break
        return leng, palinromic

    def generate_odd_s(self, s):
        tmp_s = '#'
        for i in range(len(s)):
            tmp_s += (s[i] + '#')
        return tmp_s

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length_s = len(s)
        longest_par_len, palin_len = 0,0
        start, stop = 0, 0
        tmp_s = ""
        pa_str = ""
        if length_s == 0:
            pass
        else:
            tmp_s = self.generate_odd_s(s)
            length = len(tmp_s)
            for i in range(length/2):
                center_left, center_right = length/2 - i, length/2 + i
                if longest_par_len/2 >= center_left:
                    break
                palin_len, palin_str = self.is_palindromic(center_left, tmp_s)
                if palin_len > longest_par_len:
                    longest_par_len = palin_len
                    pa_str_tmp = palin_str
                    start, stop = self.start, self.stop
                palin_len, palin_str = self.is_palindromic(center_right, tmp_s)
                if palin_len > longest_par_len:
                    longest_par_len = palin_len
                    pa_str_tmp = palin_str
                    start, stop = self.start, self.stop
            pa_str = s[start/2: stop/2]
            
        return pa_str
