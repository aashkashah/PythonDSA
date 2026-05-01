
from collections import defaultdict, deque
from typing import List

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # adj list([directory[, pattern]])    
        # in-degrees(x)
        # bfs to track indegree
        
        adj_list = defaultdict(list)
        # mistake here 
        in_degree = [0] * numCourses 
        q = deque()
        count = 0
        
        for elem in prerequisites:
            child, parent = elem
            
            adj_list[parent].append(child)
            in_degree[child] += 1
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            count += 1
            
            children = adj_list[curr] 
            
            for c in children:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)
        
        return count == numCourses

    
if __name__ == "__main__":
    sol = Solution()
    res = sol.lowestCommonAncestor()
    print(res)
    