class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        last_index_a = m - 1
        last_index_b = n - 1
        last_index = m + n - 1
        while last_index_a >= 0 and last_index_b >= 0:
            if A[last_index_a] > B[last_index_b]:
                A[last_index] = A[last_index_a]
                last_index -= 1
                last_index_a -= 1
            else:
                A[last_index] = B[last_index_b]
                last_index -= 1
                last_index_b -= 1
        while last_index_b >= 0:
            A[last_index] = B[last_index_b]
            last_index -= 1
            last_index_b -= 1

