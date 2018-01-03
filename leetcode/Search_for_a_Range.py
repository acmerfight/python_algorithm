class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        mid = 0
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                break
        if nums[mid] == target:
            i = j = mid
            while i >= 0 and nums[i] == target:
                i -= 1
            while j <= len(nums) - 1 and nums[j] == target:
                j += 1
            return [i + 1, j - 1]
        else:
            return [-1, -1]
