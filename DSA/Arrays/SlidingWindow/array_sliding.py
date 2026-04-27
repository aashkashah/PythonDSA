
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
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))