class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for sub in s:
            if sub in freq:
                freq[sub]+=1
            else:
                freq[sub]=1

        for idx in range(len(s)):
            if freq[s[idx]]==1:
                return idx
        return -1