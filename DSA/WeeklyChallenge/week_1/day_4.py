from collections import deque

from DSA.Trees.LCA.tree_base import TreeNode

class week1_day4:
    
    def levelOrder(root: TreeNode):
        
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level)
        
        return result        
    
    def execution_order(dependencies):
        visited = set()
        result = []
        # visiting prevents cycles
        visiting= set()
        
        def dfs(job):
            
            if job in visiting:
                raise ValueError("cirular dependency deteced")
            
            if job in visited:
                return
            
            visiting.add(job)
            
            for dependency in dependencies[job]:
                dfs(dependency)
                
            visiting.remove(job)
            visited.add(job)
            result.append(job)
                
        return result
                    