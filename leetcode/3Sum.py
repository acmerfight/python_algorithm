class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for index, num in enumerate(nums):
            if index > 0 and nums[index - 1] == num:
                continue
            tmp_sum = 0 - num
            i = index + 1
            j = len(nums) - 1
            while i < j:
                if i > index + 1 and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j -= 1
                    continue
                if nums[i] + nums[j] == tmp_sum:
                    result.append([num, nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < tmp_sum:
                    i += 1
                else:
                    j -= 1
        return result
