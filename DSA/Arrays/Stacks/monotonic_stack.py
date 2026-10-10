class MonotonicStack:
    
    def dailyTemperatures(self, temps):
        
        n = len(temps)
        result = list[0] * n
        stack = []
        
        for i in range(n):
            while stack and temps[i] > temps[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            
            stack.append(i)
        
        return result
    
    def nextGreaterElement(self, nums):
        
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = nums[i]
            stack.append(i)
            
        return result
    