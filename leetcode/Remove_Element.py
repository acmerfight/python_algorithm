# https://leetcode.com/problems/remove-element/

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        current_index = 0
        for index in xrange(len(nums)):
            if val != nums[index]:
                nums[current_index] = nums[index]
                current_index += 1
        return len(nums[:current_index])
