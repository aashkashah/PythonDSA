from typing import List

class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = [] ##List[List[int]] -- wrong way, default [] works
         
        intervals.sort()
        
        leftPtr = 0
        
        while leftPtr < len(intervals):
            start = intervals[leftPtr][0]
            end = intervals[leftPtr][1]
            
            rightPtr = leftPtr + 1
            
            while rightPtr < len(intervals) and intervals[rightPtr][0] <= end:
                end = max(end, intervals[rightPtr][1])
                rightPtr += 1
            
            res.append([start, end])
            
            leftPtr = rightPtr
        
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    