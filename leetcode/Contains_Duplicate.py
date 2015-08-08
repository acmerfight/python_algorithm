# https://leetcode.com/submissions/detail/35659875/


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return not (len(set(nums)) == len(nums))
