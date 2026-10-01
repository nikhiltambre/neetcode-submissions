class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #things that come in mind
        #1 nested loop with O(n^2) time and constant space
        # result=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         sum=nums[i]+nums[j]
        #         if sum==target:
        #            return [i,j]
        
        # return result
        
        entity={}
        #Using hashmap:
        
        for i,n in enumerate(nums):
            diff=target-n
            if diff in entity :
                return [entity[diff],i] 
            entity[n]=i
