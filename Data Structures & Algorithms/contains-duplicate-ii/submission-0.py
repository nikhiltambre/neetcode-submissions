class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #----brute force---:
        # TC-> O(N^2) and Sc-> O(1) 
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True
        return False
