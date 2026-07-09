class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for pair in prerequisites:
            u, v = pair
            graph[v].append(u)

        state = [0] * numCourses

        def dfs(graph, node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for neighbor in graph[node]:
                if not dfs(graph, neighbor):
                    return False

            state[node] = 2
            return True
            
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(graph, course):
                    return False

        return True

                

