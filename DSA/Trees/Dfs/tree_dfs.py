from typing import List

from DSA.Trees.LCA.tree_base import TreeNode

class Solution:
    
    def pathSum2(self, root: TreeNode, target: int) -> List[List[int]]:
        
        def dfs(node, target, path):
            if node is None:
                return
            
            path.append(node.val)
            if not node.left and not node.right:
                if node.val == target:
                    result.append(path.copy())

            dfs(node.left, target - node.val, path)
            dfs(node.right, target -node.val, path)
            path.pop()
            
        result = []
        dfs(root, target, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    res = sol.pathSum2()
    print(res)
        