class StackQues:
    
    def isValid(self, s):
        
        # use stack 
        stack = list[str]
        
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # if it's a closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # opening bracket
                stack.append(char)
        
        # valid if all brackets are matched 
        return len(stack) == 0
    
    def decodeString(self, s):
        stack = []
        curr_string = ""
        current_number = 0
        
        for char in s:
            if char == "[":
                stack.append(curr_string)
                stack.append(current_number)
                curr_string = ""
                current_number = 0
            elif char == "]":
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + num * curr_string
            else:
                curr_string += char
        
        return curr_string
    
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
                