class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # i have to find the days where no meeting is there i might think merging the meeting days after sorting them
        

        meetings.sort(key=lambda x:x[0])
        merged = [meetings[0]]

        for rem in meetings[1:]:
            last = merged[-1]

            if last[1]>=rem[0]:
                last[1]=max(last[1],rem[1])
            else:
                merged.append(rem)
        
        n = 0
        for meets in merged:
            n+=(meets[1]-meets[0])+1
        
        return days-n
