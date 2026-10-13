class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        result = []

        def permutations(ans):
            if len(ans) == len(nums):
                if ans not in result:
                 result.append(ans.copy())
                return
            for i in range(len(nums)):
                if not visited[i]:
                    ans.append(nums[i])
                    visited[i] = True
                    permutations(ans)
                    ans.pop()
                    visited[i] = False
        permutations([])
        return result