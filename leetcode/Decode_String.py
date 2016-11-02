class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        int_stack = []
        str_stack = []
        res = ""
        i = 0
        count = 0
        while i < len(s):
            if s[i].isdigit():
                count = count * 10 + int(s[i])
                i += 1
            elif s[i] == "[":
                int_stack.append(count)
                count = 0
                str_stack.append(res)
                res = ""
                i += 1
            elif s[i] == "]":
                res = str_stack.pop() + (int_stack.pop() * res)
                i += 1
            else:
                res += s[i]
                i += 1
        return res

