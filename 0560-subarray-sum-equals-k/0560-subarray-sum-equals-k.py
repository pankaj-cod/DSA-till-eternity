class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # We can check all subarrays then count if the sum equals k
        freq = {0:1} # freq of prefix sums 
        # prefix[j]-prefix[i]=k
        # prefix[i] = prefix[j]-k we calculate how many times each prefix sum has occured 

        n = len(nums)
        ans = 0
        prefix = 0
        for num in nums:
            prefix += num

            needed = prefix-k

            if needed in freq:
                ans += freq[needed]
            
            if prefix in freq:
                freq[prefix]+=1
            else:
                freq[prefix]=1
        return ans
            
