
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count_nums1 = {}
        count_nums2 = {}
        for num in nums1:
            count_nums1[num] = count_nums1.get(num, 0) + 1
        for num in nums2:
            count_nums2[num] = count_nums2.get(num, 0) + 1
        res = []
        for num in (set(nums1) & set(nums2)):
            if count_nums1[num] < count_nums2[num]:
                res.extend(count_nums1[num] * [num])
            else:
                res.extend(count_nums2[num] * [num])
        return res

