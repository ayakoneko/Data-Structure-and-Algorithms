class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1]) 
        removed = 0
        end = intervals[0][1]

        for s, e in intervals[1:]:
            if s < end:         
                removed += 1     
            else:
                end = e          

        return removed
        