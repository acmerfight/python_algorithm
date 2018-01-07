import heapq

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        heap = []
        for index, num in enumerate(nums):
            if index < k:
                heapq.heappush(heap, num)
            else:
                num_b = heapq.heappop(heap)
                if num > num_b:
                    heapq.heappush(heap, num)
                else:
                    heapq.heappush(heap, num_b)
        return heapq.heappop(heap)



