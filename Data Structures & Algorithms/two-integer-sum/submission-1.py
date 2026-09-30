class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #things that come in mind
        #1 nested loop with O(n^2) time and constant space
        #2 sort array and use two pointers
        #3  
        result=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==target:
                   return [i,j]
        
        return result