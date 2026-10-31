from collections import deque


class Solution:
    def foreignDictionary(self, dict: List[str]) -> str:
        # construct DAG
        chars=set("".join(dict))
        K=26
        N = len(dict)
        adj = [[] for _ in range(K)]
        for i in range(N - 1):
            first, second = dict[i], dict[i + 1]
            if len(first)>len(second) and first.startswith(second):
                return ""
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    adj[ord(first[j]) - ord("a")].append(ord(second[j]) - ord("a"))
                    break
        # calculate indegrees
        indegree = [0] * K
        for node in range(K):
            for v in adj[node]:
                indegree[v] += 1

        # push indegrees 0 to queue
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0 and chr(i+ord("a")) in chars:
                queue.append(i)

        # find toposort
        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        # cycle detection
        if len(topo)!=len(chars):
            return ""
        return "".join(chr(x+ord("a")) for x in topo)
