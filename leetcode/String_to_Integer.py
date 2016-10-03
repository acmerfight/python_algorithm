class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        if not str:
            return result
        i = 0
        while str[i] == " ":
            i += 1
        sign = +1
        if str[i] == "+" or str[i] == "-":
            sign = int(str[i] + "1")
            i += 1
        for char in str[i:]:
            if char.isdigit():
                result = int(result) * 10 + int(char)
            else:
                break
        result *= sign
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result
