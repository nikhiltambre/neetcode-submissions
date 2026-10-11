class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def generateSubsets(i, ans):
            if i == len(nums):
                result.append(ans)
                return 
            generateSubsets(i + 1, ans + [nums[i]])
            generateSubsets(i + 1, ans)

        generateSubsets(0,[])
        return result
