
from typing import List


class Solution:
    
    def findCircelNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        
        # c# style, not correct
        #parent = List[n]
        
        parent = []
        for i in range(n):
            parent.append(i)
        
        for i in range(n):
            for j in range(i, n):
                
                if isConnected[i][j] == 1:
                    rootA = self.Find(parent, i)
                    rootB = self.Find(parent, j)
                
                    # for integers use !=, for value comparison use 'i's not'
                    if rootA != rootB:
                        parent[rootA] = rootB
        
        components = 0
        
        for i in range(n):
            if parent[i] == i:
                components += 1
        
        return components
    
    def Find(self, parent: List[int], node: int ) -> int:
        
        while parent[node] != node:
            node = parent[node]
        return node

if __name__ == "__main__":
    sol = Solution()
    res = sol.findCircelNum() 
    print(res)