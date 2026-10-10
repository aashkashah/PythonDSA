
from typing import List

class Solution:
    
    ### fixed length ###
    def max_subarray_sum(nums, k):
        max_sum = float('-inf')
        window = 0
        start = 0
        
        for end in range(len(nums)):
            window += nums[end]
            
            if end - start + 1 == k:
                max_sum = max(max_sum, window)
                window -= nums[start]
                start += 1
        
        return max_sum
    
    ### inverse fixed length ###
    def max_score(cards, k):
        total = sum(cards)
        if k == len(cards):
            return total
        
        window = 0
        max_points = 0
        start = 0
        
        for end in range(len(cards)):
            state += cards[end]
            
            if end - start + 1 == len(cards) - k:
                max_points = max(total - window, max_points)
                state -= cards[start]
                start += 1
        
        return max_points
    
    ### variable length ###
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set()
        maxWindow = 0
        left = 0
        right = 0
        
        for right in range(len(s)):
            
            # if s[right] not in window:
            #     window.add(s[right])
            # else:
            while s[right] in window:
                window.remove(s[left])
                left += 1
                     
            window.add(s[right])
            maxWindow = max(maxWindow, right - left + 1)
        
        return maxWindow
    
    def longestSubstringWithoutRepeat(self, s: str) -> int:
        
        window = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            if s[right] in window: 
                while s[right] in window: 
                    window.discard(s[left])
                    left += 1
            
            window.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))