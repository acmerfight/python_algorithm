class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0
        end = len(letters) - 1
        while start < end:
            mid = start + (end - start) / 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid
        return letters[0] if letters[end] <= target else letters[end]
