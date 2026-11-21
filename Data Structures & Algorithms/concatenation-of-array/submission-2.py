class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
      n=len(nums) 
      newArray=[num for num in nums]
      for num in nums:
        newArray.append(num)
      return newArray