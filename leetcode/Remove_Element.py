class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        copy_data = nums[:]
        for index in xrange(len(nums)):
            if nums[index] == val:
                copy_data.remove(val)
        return len(copy_data)


print Solution().removeElement([4, 5], 4)
