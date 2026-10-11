class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def allsubsets(i,total):
            if i==len(nums):
                return total
            return allsubsets(i+1,total^nums[i])+allsubsets(i+1,total)  
        return allsubsets(0,0)