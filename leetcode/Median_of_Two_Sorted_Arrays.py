#There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time 
#complexity should be O(log (m+n)).

# O(m+n) but can be accepted
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        total_len = len(A) + len(B)
        if total_len & 1:
            return self.find_kth(A, B, total_len / 2 + 1)
        else:
            return (self.find_kth(A, B, total_len / 2) + self.find_kth(A, B, total_len / 2 + 1)) / 2.0
                        
    @staticmethod
    def find_kth(A, B, k):
        index = 0
        index_a = 0
        index_b = 0
        while index_a < len(A) and index_b < len(B):
            if A[index_a] >= B[index_b]:
                index += 1
                if index == k:
                    return B[index_b]
                index_b += 1
            else:
                index += 1
                if index == k:
                    return A[index_a]
                index_a += 1

        while index_a < len(A):
            index += 1
            if index == k:
                return A[index_a]
            index_a += 1

        while index_b < len(B):
            index += 1
            if index == k:
                return B[index_b]
            index_b += 1
