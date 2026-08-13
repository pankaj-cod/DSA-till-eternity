class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        n = len(nums)
        def helper(i,arr):
            if i>=n:
                if len(arr)>=2 and arr not in ans and sorted(arr)==arr:
                    seen = arr
                    ans.append(arr[:])
                    return
                return
            arr.append(nums[i])
            helper(i+1,arr)
            arr.pop()
            helper(i+1,arr)
        helper(0,[])
        ans.sort(key=lambda x:len(x))
        return ans