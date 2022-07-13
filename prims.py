class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        visited = [False] * size
        pq = []
        
        x1, y1 = points[0]
        for i in range(1, size):
            x2, y2 = points[i]
            cost = abs(x2 - x1) + abs(y2 - y1)
            pq.append((cost, 0, i))
            
        heapq.heapify(pq)
        
        count = size - 1
        res = 0
        visited[0] = True
        while pq and count > 0:
            cost, point1, point2 = heapq.heappop(pq)
            if not visited[point2]:
                res += cost
                visited[point2] = True
                count -= 1
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0] - points[j][0]) + abs(points[point2][1] - points[j][1])
                        heapq.heappush(pq, (distance, point2, j))
        return res
