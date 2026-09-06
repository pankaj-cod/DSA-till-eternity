class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        smaller = []
        larger = []
        hmap = {}
        hmap2 = {}
        ans = []
        if len(nums1)>len(nums2):
            smaller = nums2
            larger = nums1
        else:
            smaller = nums1
            larger = nums2
        for num in smaller:
            if num in hmap:
                hmap[num]+=1
            else:
                hmap[num]=1
        for num in larger:
            if num in hmap2:
                hmap2[num]+=1
            else:
                hmap2[num]=1
        for num in hmap:
            if num in hmap2:
                for _ in range(min(hmap[num],hmap2[num])):
                    ans.append(num)
        return ans

        