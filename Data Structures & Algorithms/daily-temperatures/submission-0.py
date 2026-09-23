class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = deque()
        ans = [0]*n
        for j in range(n):
            while stack and temperatures[stack[-1]] < temperatures[j]:
                prev_index = stack.pop()
                ans[prev_index] = j - prev_index
            stack.append(j)
        return ans
