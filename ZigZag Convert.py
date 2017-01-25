"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility) """
"""input abcefghijklmnopqrstu"""
"""a     g      m     s"""
"""b   f h    l n   r t"""
"""c e   i  k   o q   u"""
"""d     j      p      """
"""output is agmsbfhlnrtceikoqudjp"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_list = ['' for i in range(numRows)]
        target_str = ''
        length = len(s)
        row = 0
        column = 0
        if length == 0 or numRows == 1:
            return s
        for i in range(length):
            str_list[row] += s[i]
            if column%(numRows - 1) == 0:
                if row == numRows - 1:
                    column += 1
                    row -= 1
                else:
                    row += 1
                continue
            else:
                row -= 1
                column += 1
   
        for j in range( numRows ):
            target_str += str_list[j]
        return target_str    
