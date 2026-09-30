from DSA.Trees.LCA.tree_base import TreeNode


class BottomUp:
    
    def pathSum(self, root, target):
        if root is None:
            return False
        
        if not root.left and not root.right:
            return target == root.val
        
        target -= root.val
        
        return self.pathSum(root.left, target) or self.pathSum(root.right, target)
    
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return 1 + max(left, right)