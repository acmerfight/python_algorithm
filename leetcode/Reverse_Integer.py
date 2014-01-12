#Reverse digits of an integer.

#Example1: x = 123, return 321
#Example2: x = -123, return -321

class Solution:
    # @return an integer
    def reverse(self, x):
        if x < 0:
            return 0 - int(str(x)[1:][::-1])
        else:
            return int(str(x)[::-1])
