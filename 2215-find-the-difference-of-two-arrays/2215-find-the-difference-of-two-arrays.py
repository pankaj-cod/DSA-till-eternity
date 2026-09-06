class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        lst1 = set(nums1)
        lst2 = set(nums2)
        ans = []
        ans.append(list(lst1.difference(lst2)))
        ans.append(list(lst2.difference(lst1)))
        return ans