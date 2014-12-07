class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if not digits:
            return []
        reversed_digits = list(reversed(digits))
        for index, number in enumerate(reversed_digits):
            if number < 9:
                number += 1
                digits[-1 - index] = number
                return digits
            if number >= 9:
                number = 0
                if len(reversed_digits) == index + 1:
                    digits.insert(0, 1)
            digits[-1 - index] = number
            self.plusOne(digits[index+1:])
        return digits
