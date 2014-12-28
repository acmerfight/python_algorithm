

# may be have bug can't ac
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        return self.perm(num, 0, len(num))

    def perm(self, pool, start, end, result=[]):
        if start >= end:
            result.append(pool[:])
        for i in xrange(start, end):
            pool[start], pool[i] = pool[i], pool[start]
            self.perm(pool, i+1, end)
            pool[i], pool[start] = pool[start], pool[i]
        return result

print Solution().permute([0, 1])


class Solution:
    def permute(self, nums):
        solutions = [[]]
        for num in nums:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    next.append(solution[:i] + [num] + solution[i:])
            solutions = next
        return solutions
