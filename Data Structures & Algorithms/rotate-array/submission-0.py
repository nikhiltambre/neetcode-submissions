class Solution:
    def reverseLs(self, nums: List[int], s: int, e: int):
        while s <= e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.reverseLs(nums, 0, len(nums) - 1)
        self.reverseLs(nums, 0, k - 1)
        self.reverseLs(nums, k, len(nums) - 1)
