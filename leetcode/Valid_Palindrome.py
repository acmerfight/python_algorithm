class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        data = [letter.upper() for letter in s if (letter.isalpha() or letter.isdigit())]
        if len(data) < 2:
            return True
        length = len(data)
        for i in xrange(length/2):
            if data[i] != data[-1-i]:
                return False
        return True
