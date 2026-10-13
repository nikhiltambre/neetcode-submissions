class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def generateSubsets(i, ans):
            if i == len(nums):
                result.append(ans)
                return 
            generateSubsets(i + 1, ans + [nums[i]])
            j=i+1
            while j<len(nums) and nums[j]==nums[i]:
                j+=1
            generateSubsets(j, ans)

        generateSubsets(0,[])
        return result
 