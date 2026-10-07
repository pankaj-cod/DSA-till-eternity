class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mex = max(nums)
        ans = 0
        positions = []

        for i in range(len(nums)):
            if nums[i] == mex:
                positions.append(i)

        if len(positions) < k:
            return 0

        for p in range(len(positions)):
            if p + k - 1 < len(positions):
                thresh = positions[p + k - 1]

                if p == 0:
                    left_count = positions[p] + 1
                else:
                    left_count = positions[p] - positions[p - 1]

                ans += left_count * (n - thresh)

        return ans