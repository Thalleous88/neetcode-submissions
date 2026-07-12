class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append([flight[1], flight[2]])

        
            
        def dp(graph, node, dst):
            visited = set()
            queue = deque([[node, 0, 0]])
            best = float('inf')
            visited.add(node)
            
            while queue:
                
                current, cost, path = queue.popleft()
                
                

                for neighbor in graph[current]:
                    if neighbor[1] + cost > best:
                        continue
                    
                    if path > k:
                        continue
                    elif neighbor[0] == dst and ((neighbor[1] + cost) < best) and path <= k:
                        print(current, cost, path)
                        best = neighbor[1] + cost

                    if tuple([neighbor[0], neighbor[1], path]) not in visited:
                        visited.add(tuple([neighbor[0], neighbor[1], path]))
                        queue.append([neighbor[0], cost + neighbor[1], path + 1])

            if best == float('inf'):
                return -1

            return best
       

        return dp(graph, src, dst)