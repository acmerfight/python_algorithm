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
