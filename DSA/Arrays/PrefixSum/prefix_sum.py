from collections import defaultdict
from typing import List

class Solution:
    
    # subarray sum equls k
    def subarrySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        
        prefix_counts = defaultdict(int)
        
        for num in nums:
            prefix += num
            
            if prefix == k:
                count += 1
                
            # if (sum - k) in map:
            #     v = map[(sum - k)]
            #     count += v    
            count += prefix_counts[prefix - k]
                
            # if (sum) not in map:
            #     map[sum] = 1
            # else:
            #     map[sum] += 1
            prefix_counts[prefix] += 1
        
        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarrySum([1, 1, 1], 2))