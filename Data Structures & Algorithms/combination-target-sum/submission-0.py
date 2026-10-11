class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def combFinding(i, ans, total):
            if total == target:
                nonlocal result
                result.append(ans)
                return
            if i == len(nums) or total>target:
                return
            
            combFinding(i , ans + [nums[i]], total + nums[i])
            combFinding(i + 1, ans, total)

        combFinding(0, [], 0)
        return result
