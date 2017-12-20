class Solution(object):
    @staticmethod
    def _count_lower(data, number):
        start = 0
        end = len(data)
        while start < end:
            mid = start + (end - start) / 2
            if number >= data[mid]:
                start = mid + 1
            elif number < data[mid]:
                end = mid
        return start

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low, high = matrix[0][0], matrix[-1][-1]
        while low <= high:
            mid = low + (high - low) / 2
            less_count = sum(self._count_lower(m, mid) for m in matrix)
            if less_count >= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        q = [(matrix[0][0], 0, 0)]
        ans = None
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < n:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans
