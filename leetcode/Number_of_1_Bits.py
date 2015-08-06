
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        val = 0
        while n:
            if  n % 2 == 1:
                val += 1
            n /= 2
        return val
