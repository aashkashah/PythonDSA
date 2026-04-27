from typing import List
from collections import Counter
import heapq

class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
    
        # build hash map
        count = Counter(nums)
        
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])
    
        result.reverse()
        
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))