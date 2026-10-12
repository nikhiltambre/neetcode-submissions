class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        memo = {}

        def combFinding(i, total):
            if total == target:
                return [[]]

            if i == len(nums) or total+nums[i] > target:
                return []

            if (i, total) in memo:
                return memo[(i, total)]

            take = [[nums[i]]+c for c in combFinding(i + 1, total + nums[i])]

            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            skip = combFinding(j, total)

            memo[(i, total)] = take + skip
            
            return memo[(i, total)]

        return combFinding(0, 0)
