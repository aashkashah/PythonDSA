class RootToLeaf:
    
    def goodNodes(self, root):
        
        count = 0
        
        def dfs(node, max_so_far):
            nonlocal count
            if not node:
                return 
            if node.val >= max_so_far:
                count += 1
            new_max = max(max_so_far, node.val)
            dfs(node.left, new_max)
            dfs(node.right, new_max)
            
        dfs(root, float('-inf'))
        return count
    
    def pathSum(self, root, target):
        def dfs(node, target, path):
            if not node:
                return
        
            path.append(node.val)
            if not node.left and not node.right:
                if node.val == target:
                    result.append(path[:])
            
            dfs(node.left, target - node.val, path)
            dfs(node.right, target - node.val, path)
            path.pop()
                    
        result = []
        dfs(root, target, [])
        return result
    
    def longestUnivaluePath(self, root):
        max_length = 0
        
        def dfs(node):
            nonlocal max_length
            if not node:
                return 0
            
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            left_arrow = right_arrow = 0
            
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
                
            max_length = max(max_length, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        
        dfs(root)
        return max_length
    
    
     
    
            