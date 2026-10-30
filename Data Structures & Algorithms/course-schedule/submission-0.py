class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct dag
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)

        # find indegrees
        indegree = [0] * numCourses
        for i in range(numCourses):
            for v in adj[i]:
                indegree[v] += 1

        # pusing nodes with zero indegrees
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        cnt = 0
        while queue:
            node = queue.popleft()
            cnt += 1
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return True if cnt == numCourses else False
        pass
