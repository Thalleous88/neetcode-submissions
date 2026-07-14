class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = defaultdict(list)
        reverse = defaultdict(list)

        if len(edges) == 0 and n == 1:
            return True

        

        for edge in edges:
            u, v = edge
            adj[u].append(v)
            reverse[v].append(u)
            
        
            
        
        def bfs(node, dct):
            visited = set()
            queue = deque()

            visited.add(node)
            queue.append(node)

            connection = 0
            while queue:
                curr = queue.popleft()
                
                if curr not in dct:
                    continue
                for neighbor in dct[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

                    else:
                        return False

                    connection += 1

            if connection != n-1:
                return False
            return True


        for num in adj.keys():
            print(len(adj))
            if bfs(num, adj) is True:
                return True
        
        for num in reverse.keys():
            if bfs(num, reverse) is True:
                return True

        return False


        