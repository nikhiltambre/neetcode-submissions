class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False] * len(nums)
        result = []

        def permutations(ans):
            if len(ans) == len(nums):
                result.append(ans.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i>0 and nums[i-1]==nums[i] and not visited[i-1]:
                    continue
                visited[i] = True
                ans.append(nums[i])
                permutations(ans)
                ans.pop()
                visited[i] = False

        permutations([])
        return result
