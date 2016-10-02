class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        i = 0
        for char in str:
            if char == " ":
                i += 1
            else:
                break
        result = ""
        if str[i] in ("+", "-"):
            result = str[i]
            i += 1
        for char in str[i:]:
            if char.isdigit():
                result += char
            else:
                break
        print result, "xx"
        if (len(result) == 1 and result in "-+") or not result:
            return 0
        if int(result) > 2147483647:
            return 2147483647
        if int(result) < -2147483648:
            return -2147483648
        return int(result)

