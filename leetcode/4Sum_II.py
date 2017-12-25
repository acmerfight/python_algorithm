from collections import Counter


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        cnt = Counter()
        for a in A:
            for b in B:
                cnt[a+b] += 1
        res = 0
        for c in C:
            for d in D:
                res += cnt[-(c + d)]
        return res
