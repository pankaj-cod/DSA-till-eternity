class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans = []
        for num in freq.keys():
            if freq[num]>n//3:
                ans.append(num)

        return ans