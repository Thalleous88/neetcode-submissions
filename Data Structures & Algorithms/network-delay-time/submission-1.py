class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for time in times:
            u, v, cost = time
            adj[u].append((v, cost))
        
        def bfs(node):
            distance = {n: float('inf') for n in range(1, n+1)}
            distance[node] = 0
            pq = [(0, node)]
            heapq.heapify(pq)


            while pq:
                cost, curr = heapq.heappop(pq)
                for neighbor in adj[curr]:
                    v, c = neighbor

                    tot = c + cost
                    
                    if distance[v] > tot:
                        distance[v] = tot
                        heapq.heappush(pq, (tot, v))

            
            if max(distance.values()) == float('inf'):
                return -1

            return max(distance.values())


        return bfs(k)