class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum = A[0]
        tmp_sum = A[0]
        for number in A[1:]:
            if tmp_sum > 0:
                tmp_sum += number
            else:
                tmp_sum = number
            if tmp_sum > max_sum:
                max_sum = tmp_sum
        return max_sum


class Solution1:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum = A[0]
        for index, number_a in enumerate(A):
            tmp_sum = number_a
            for number_b in A[index + 1:]:
                tmp_sum = tmp_sum + number_b
                if max_sum < tmp_sum:
                    max_sum = tmp_sum
        return max_sum



class Solution(object):

    @staticmethod
    def find_max_crossing_subarray(nums, low, mid, high):
        if low == mid:
            left_max_sum = nums[mid]
        else:
            tmp_sum = nums[mid]
            left_max_sum = nums[mid]
            for i in xrange(mid - 1, low - 1, -1):
                tmp_sum += nums[i]
                if tmp_sum > left_max_sum:
                    left_max_sum = tmp_sum

        if mid == high:
            right_max_sum = 0
        else:
            right_max_sum = 0
            tmp_sum = 0
            for i in xrange(mid + 1, high + 1):
                tmp_sum += nums[i]
                if tmp_sum > right_max_sum:
                    right_max_sum = tmp_sum
        return left_max_sum + right_max_sum

    def find_max_subarray(self, nums, low, high):
        if low == high:
            return nums[low]
        mid = (low + high) / 2
        left_sum = self.find_max_subarray(nums, low, mid)
        right_sum = self.find_max_subarray(nums, mid+1, high)
        cross_sum = self.find_max_crossing_subarray(nums, low, mid, high)
        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        return self.find_max_subarray(nums, 0, len(nums) - 1)



