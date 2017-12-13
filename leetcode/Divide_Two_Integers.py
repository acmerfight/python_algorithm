class Solution(object):

    @staticmethod
    def _positive(dividend, divisor):
        return (dividend > 0) is (divisor > 0)

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = self._positive(dividend, divisor)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while divisor <= dividend:
            temp, i = divisor, 1
            while temp <= dividend:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        res = res if positive else -res
        return min(max(-2147483648, res), 2147483647)
