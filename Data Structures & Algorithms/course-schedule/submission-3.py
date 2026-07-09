class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for pair in prerequisites:
            u, v = pair
            graph[v].append(u)


        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False


            state[course] = 2

            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False


        return True


                

