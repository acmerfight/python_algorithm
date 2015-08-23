# https://leetcode.com/problems/add-digits/


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        num_int = sum([int(i) for i in num])
        if len(str(num_int)) == 1:
            return num_int
        else:
            return self.addDigits(num_int)
