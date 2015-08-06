
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        res = ""
        while n:
            if  n % 2 == 0:
                res += "0"
            else:
                res += "1"
            n /= 2
