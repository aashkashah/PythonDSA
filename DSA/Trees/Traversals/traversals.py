
from collections import deque
from typing import List, Optional

from DSA.Trees.LCA.tree_base import TreeNode


class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # 1. build parent map using BFS
        parent = {}
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            
            if node.right:
                parent[node.right] = node
                q.append(node.right)
        
        # 2. BFS from tagret, going left/right/up 
        
        q = deque()
        q.append((target, 0))
        # to note: empty {} is a WeakKeyDictionary, 
        # something inside it makes it a set
        visited = {target}
        result = []
        
        while q:
            node, dist = q.popleft()
            
            if dist == k:
                result.append(node.val)
                continue
            
            for neighbour in [node.left, node.right, parent.get(node)]:
                if neighbour and neighbour not in visited:
                    visited.add(neighbour)
                    q.append((neighbour, dist + 1))
        
        return result

    def level_order_sum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        sums = []
        queue: deque[TreeNode] = deque([root])
        
        while queue:
            level_size = len(queue)
            sum = 0
            for i in range(level_size):
                node = queue.popleft()
                sum += node.val
                
                if i == level_size - 1:
                    sums.append(sum)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return sums
        
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.lowestCommonAncestor()
    print(res)
        