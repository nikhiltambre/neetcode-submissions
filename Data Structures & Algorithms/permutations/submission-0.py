class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        visited=[False]*len(nums) 
        def permutations(ans):
            if len(ans)==len(nums):
                result.append(ans.copy()) 
                return
            for j in range(len(nums)):
             if not visited[j]:
              visited[j]=True
              ans.append(nums[j])
              permutations(ans)
              ans.pop()
              visited[j]=False
        permutations([])
        return result
        