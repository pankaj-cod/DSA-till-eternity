class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort the intervals based on the starting position of intervals and if the second eleme is greater than 
        # the first ele of the next append it into the ans
        
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]

        for rem in intervals[1:]:
            last = merged[-1]

            if last[1]>=rem[0]:
                last[1]=max(rem[1],last[1])
            else:
                merged.append(rem)
        
        return merged