class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        
        sorted_chars = sorted(freq.keys(),key=lambda x:freq[x],reverse=True)
        ans = ""
        for char in sorted_chars:
            sub = char*freq[char]
            ans+=sub
        return ans