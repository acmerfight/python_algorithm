class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_sub_length = 0
        last_position = {}
        start = 0
        for index, char in enumerate(s):
            if char in last_position and last_position[char] >= start:
                start = last_position[char] + 1
            last_position[char] = index
            max_sub_length = max(max_sub_length, index - start + 1)
        return max_sub_length

