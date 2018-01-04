class Solution(object):

    def power(self, x, n):
        if n == 0:
            return 1
        half = self.power(x, n / 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / float(self.power(x, -n))
        else:
            return self.power(x, n)
