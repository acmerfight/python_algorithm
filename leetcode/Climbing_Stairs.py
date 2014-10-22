class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n in (1, 2):
            return n
        a, b = 1, 2
        i = 2
        while i < n:
            a, b = b, a + b
            i += 1
        return b
