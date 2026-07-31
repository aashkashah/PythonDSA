class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        
        def backtrack(start, combo, current_target):
            if current_target == 0:
                result.append(list(combo))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > current_target:
                    return
                combo.append(candidates[i])
                backtrack(i, combo, current_target - candidates[i])
                combo.pop()
        
        backtrack(0, [], target)
        return result