class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        d = 1
        while x / d >= 10:
            d *= 10
        while x > 0:
            start_number = x / d
            end_number = x % 10
            if start_number != end_number:
                return False
            x = x % d / 10
            d /= 100
        return True
