from typing import List

# container with most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            
            max_area = max(max_area, min(height[left], height[right]) * width )
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        if target == 0:
            return 0
        res = 0
        n = len(nums)
        
        if n < 3:
            return 0
        
        for i in n - 2:
            
            l = i + 1
            r = n - 1
            
            while  l < r:
                sum = nums[i] + nums[l] + nums[r]
                
                if sum < target:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        
        return res
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            
            # skip duplicate
            if i > 0 and nums[i] == nums[i -1]:
                continue
            
            l = i + 1
            r = n - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # skip duplicate
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
            
            return res
        
    def TriangeSum(nums):
        nums.sort()
        
        count = 0
        for i in range(len(nums) - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        
        return count
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
        
    