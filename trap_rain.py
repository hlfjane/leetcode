"""42. Trapping Rain Water """
"""Given n non-negative integers representing an elevation map where the width of each bar is 1"""
"""compute how much water it is able to trap after raining"""
"""example: Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6. """
"""Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6. """
"""ergodic from the highest in the center"""


class Solution(object):
    def find_the_highest(self, start, end, sample):
        highest = -1
        highest_loc = None
        for i in range(start, end):
            if sample[i] > highest:
                highest = sample[i]
                highest_loc = i
        #print "highest_loc", start, end, highest_loc
        return highest_loc
    
    def calculate_rain_area(self, start, stop, sample):
        area = 0
        #print "calculate_rain_area", start, stop
        if stop < start:
            pass
        else:
            if sample[start] >= sample[stop]:
                area = sample[stop]*(stop - start - 1)
            else:
                area = sample[start]*(stop - start - 1)
            #print "tmp area is", area
            for i in range(start + 1, stop):
                area -= sample[i]
        return area

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rain_area = 0
        length = len(height)
        start, end = 0, length-1
        if length > 1:
            highest_loc = self.find_the_highest(start, end, height)
            higher_loc = highest_loc
            start, end = 0, highest_loc
            while end > 0:
                high_loc = self.find_the_highest(start, end, height)
                rain_area += self.calculate_rain_area(high_loc, higher_loc, height)
                #print "rain_area in first while: %s "%rain_area
                start, end = 0, high_loc
                higher_loc = high_loc
                
            start, end = highest_loc + 1, length
            higher_loc = highest_loc
            while start < length - 1:
                high_loc = self.find_the_highest(start, end, height)
                rain_area += self.calculate_rain_area(higher_loc, high_loc, height)
                #print "rain_area in second while: %s "%rain_area
                start, end = high_loc + 1, length
                higher_loc = high_loc
        return rain_area

def main():
    S = Solution()
    rain_area = S.trap([2, 0, 2])
    print rain_area

main()
