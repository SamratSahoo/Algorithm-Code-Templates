class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        pq = []
        par = [i for i in range(len(points))]
        rank = [1] * len(points)
        
        def find(res):
            while res != par[res]:
                res = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
        
        def connected(n1, n2):
            return find(n1) == find(n2)
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(len(points)):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                pq.append((cost, i, j))
                
        heapq.heapify(pq)
        
        result = 0
        count = len(points) - 1
        while pq and count > 0:
            cost, i, j = heapq.heappop(pq)
            if not connected(i, j):
                union(i, j)
                result += cost
                count -= 1
                
        return result
