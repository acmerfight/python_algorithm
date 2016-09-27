class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count = {}
        t_count = {}
        if len(s) == len(t):
            for s_letter, t_letter in zip(s, t):
                s_count[s_letter] = s_count.get(s_letter, 0) + 1
                t_count[t_letter] = t_count.get(t_letter, 0) + 1
            if s_count == t_count:
                return True
            else:
                return False
        else:
            return False

