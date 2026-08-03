class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        #this is pretty easy first we inset the new interval in the intervals then we merged them

        intervals.append(newInterval)

        intervals.sort(key=lambda x:x[0])

        merged = [intervals[0]]
        for rem in intervals[1:]:
            last = merged[-1]

            if rem[0]<=last[1]:
                last[1]=max(rem[1],last[1])
            else:
                merged.append(rem)
        
        return merged