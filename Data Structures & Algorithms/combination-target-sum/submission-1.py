class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        memo = {}

        # dp solution ()
        def combFinding(i, total):
            if total == target:
                return [[]]

            if i == len(nums) or total > target:
                return []

            if (i, total) in memo:
                return memo[(i, total)]

            take = [[nums[i]] + c for c in combFinding(i, nums[i] + total)]

            miss = combFinding(i + 1, total)

            memo[(i, total)] = take + miss
            
            return memo[(i, total)]

        return combFinding(0, 0)
