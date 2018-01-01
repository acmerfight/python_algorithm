class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        res = 0
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i] > res:
                res = dp[i]
        return res



class Solution(object):

    @staticmethod
    def _insert_number(data, number):
        if number > data[-1]:
            data.append(number)
            return
        start = 0
        end = len(data) - 1
        while start < end:
            mid = start + (end - start) / 2
            if number > data[mid]:
                start = mid + 1
            else:
                end = mid
        data[end] = number

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        data = [nums[0]]
        for num in nums[1:]:
            self._insert_number(data, num)
        return len(data)

