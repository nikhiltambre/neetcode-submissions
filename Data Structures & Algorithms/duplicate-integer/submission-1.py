class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       temp=set()
       for num in nums:
          temp.add(num)
       return len(nums)>len(temp) 