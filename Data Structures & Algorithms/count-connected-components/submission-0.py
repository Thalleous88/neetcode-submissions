class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        count = 0

        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        print(adj)
        return count


