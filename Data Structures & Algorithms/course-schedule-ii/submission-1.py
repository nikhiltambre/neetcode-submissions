class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
         # construct dag
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        
        # find indegrees
        indegree=[0]*numCourses
        for i in range(numCourses):
            for v in adj[i]:
                indegree[v]+=1

        # pusing nodes with zero indegrees
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        topo=[]
        while queue:
            node=queue.popleft()
            topo.append(node)
            for v in adj[node]:
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)
        return topo if len(topo)==numCourses else  []