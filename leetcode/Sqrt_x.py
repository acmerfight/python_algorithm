class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        pre_res = None
        res = x / 2.0
        while res != pre_res:
            pre_res = res
            res = x / (2.0 * pre_res) + pre_res / 2.0
        return int(res)

