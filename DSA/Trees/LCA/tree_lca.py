from DSA.Trees.LCA.tree_base import TreeNode

class Solution:
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        self._root = root
        
        def Helper(node: TreeNode):
            
            if node is None:
                return None
            
            # use is when comparing object identity
            # use == when comparing values
            if node is p or node is q:
                return node
            
            l = Helper(node.left)
            r = Helper(node.right)
            
            if l is not None and r is not None:
                return node
            
            return l if l is not None else r
        
        return Helper(root)
        
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.lowestCommonAncestor()
    print(res)
    