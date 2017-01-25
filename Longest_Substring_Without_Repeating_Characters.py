"""Given a string, find the length of the longest substring without repeating characters."""
"""Given "abcabcbb", the answer is "abc", which the length is 3."""
"""Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring."""
"""s[0:0] is empty, s[0:1] == s[0], [i,j)"""
class Solution(object):
    def __init__(self):
        pass
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        len_s = len(s)
        len_non_repeat = len(list(set(s)))
        len_of_longest = 1
        len_tmp = 1
        sub_start, sub_end = 0, 0
        for i in range(1, len_s):
            sub_str = s[sub_start:sub_end + 1]
            
            if s[i] not in sub_str:
                sub_end = i
                len_tmp += 1
            else:
                sub_index = sub_str.find(s[i])
                sub_start = sub_start + sub_index + 1
                sub_end = i
                if len_tmp > len_of_longest:
                    len_of_longest = len_tmp
                    if len_of_longest == len_non_repeat:
                        break
                len_tmp = len_tmp - sub_index

        if len_tmp > len_of_longest:
            len_of_longest = len_tmp

        return len_of_longest


def main():
    s = "cdd"
    test = Solution()
    len = test.lengthOfLongestSubstring(s)
    print len

main()
