class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        dummy = []
        dummy[:] = nums[:]
        nots = 0 
        def digisum(x):
            ans = 0 
            while x>0:
                ans+=x%10
                x//=10
            return ans
        digi = {}

        for i in nums:
            digi[i]=digisum(i)
        
        dummy.sort(key= lambda x:digi[x])
        order = sorted(range(n), key=lambda i: (digisum(nums[i]), nums[i]))

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or order[i] == i:
                continue

            cycle_len = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = order[j]
                cycle_len += 1

            swaps += cycle_len - 1

        return swaps


        # hints suggest to calculate no of cycles in this dummy permutation

        

