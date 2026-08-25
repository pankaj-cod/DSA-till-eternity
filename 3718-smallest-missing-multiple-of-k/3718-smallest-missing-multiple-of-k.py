class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dihh = set()

        for i in nums:
            dihh.add(i)
        multis = [i*k for i in range(1,102)]

        for mul in multis:
            if mul not in dihh:
                return mul