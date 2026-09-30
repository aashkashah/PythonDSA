
from typing import List

class Solution:
    
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