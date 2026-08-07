class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = {}
        for word in words:
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
        ans = []
        
        # bucket sort creating buckets for words with same freqs
        buckets = [[] for _ in range(len(words)+1)]

        for word,f in freq.items():
            buckets[f].append(word)
        
        for bucket in buckets:
            bucket.sort() # alphabetical order
        
        for f in range(len(buckets)-1,0,-1):
            for words in buckets[f]:
                ans.append(words)
                if len(ans)==k:
                    return ans
        