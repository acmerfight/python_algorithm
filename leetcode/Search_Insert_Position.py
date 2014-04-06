class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer

    @staticmethod
    def index(A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start


    def searchInsert(self, A, target):
        return self.index(A, target)
