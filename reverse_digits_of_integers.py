"""get the number of digits and reverse them"""
"""Reverse digits of an integer."""
"""Example1: x = 123, return 321"""
"""Example2: x = -123, return -321"""
"""think of the overflow of numbers, if overflow happens, return 0"""
class Solution(object):
    def __init__(self):
        pass
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits_list = []
        tmp = x
        target = 0
        if tmp < 0:
            tmp = 0 - x
        while tmp != 0:
            digit = tmp%10
            digits_list.append(digit)
            tmp = tmp/10
        digits_list.reverse()
        if digits_list:
            for i in range(len(digits_list)):
                target += (digits_list[i]*pow(10,i))
            if x < 0:
                target = 0-target
            if target > pow(2,31) or target < -1*pow(2,31) + 1:
                target = 0
                
        return target
