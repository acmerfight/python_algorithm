class Solution(object):

    @staticmethod
    def _count_lower(nums, mid):
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        return count

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) / 2
            count = self._count_lower(nums, mid)
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return high

