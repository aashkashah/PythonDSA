import math
from typing import List


class Solution:
    
    def minHarvetRate(self, apples: List[int], h: int) -> int:
        
        def time_taken(rate):
            time = 0
            
            for i in range(len(apples)):
                #time += (apples[i] + rate - 1) // rate
                time += math.ceil(apples[i] / rate)
            return time
        
        left, right = 1, max(apples)
        
        while left < right:
            mid = (left + right) // 2
            if time_taken(mid) > h:
                left = mid + 1
            else:
                right = mid
                
        return left    
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.minHarvetRate()
    print(res)