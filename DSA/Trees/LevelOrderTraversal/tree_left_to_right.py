from collections import defaultdict
from collections import deque
from typing import List
from DSA.Trees.LCA.tree_base import TreeNode

class Solution:
    
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        # needs a type
        # empty dictionary raises a keyError
        cols = defaultdict(list) # missed adding type -- auto creates list of new keys
        
        q = deque()
        q.append((root, 0)) # similar to c#, tuple s
        mincol = float('inf') # int.maxValue
        maxcol = float('-inf') # int.MinValue
        
        while q:  # wrote this -- q is not None:
            node, column = q.popleft()
            cols[column].append(node.val)
            
            if node.left is not None:
                q.append((node.left, column - 1))
                mincol = min(mincol, column - 1)
            
            if node.right is not None:
                q.append((node.right, column + 1))
                maxcol = max(maxcol, column + 1)
           
        result = []
        for c in range(mincol, maxcol + 1):
            result.append(cols[c]) 
        return result
       
            
if __name__ == "__main__":
    sol = Solution()
    res = sol.lowestCommonAncestor()
    print(res)    
                
                
            
        
        
        
        
    