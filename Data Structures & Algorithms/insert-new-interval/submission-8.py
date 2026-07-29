class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new = []
        pos = 0
        j = 0
        check = True
        for i in range(len(intervals)):
            if j > i or (j == i and i != 0):
                continue
            if intervals[i][1] < newInterval[0]:
                pos = i+1
            if intervals[i][1] < newInterval[0] or intervals[i][0] > newInterval[1]:
                new.append(intervals[i])
            else:
                j = i
                
                start, end = min(newInterval[0], intervals[i][0]), newInterval[1]
                
                while j < len(intervals) and intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                    j += 1

                j-= 1
                    
                
                new.append(list([start, end]))

                check = False
            

        if check:
            new.insert(pos, newInterval)
        return new

        