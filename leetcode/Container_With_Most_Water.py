#Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such 
#that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the 
#container contains the most water.
#
#Note: You may not slant the container.

class Solution:
    # @return an integer
    def maxArea(self, height):
        if len(height) == 0 or len(height) == 1:
            return 0
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            min_height = min(height[start], height[end]) 
            area = min_height * (end - start)
            max_area = area if area > max_area else max_area
            if min_height == height[start]:
                start += 1
            else:
                end -= 1
        return max_area

