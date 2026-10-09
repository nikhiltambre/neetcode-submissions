class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #----brute force---:
        # TC-> O(N^2) and Sc-> O(1) 
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]==nums[j] and abs(i-j)<=k:
        #             return True
        # return False

        #---better solution ---
        # Using hashmaps
        # visited={}
        # for i in range(len(nums)):
        #     if nums[i] in visited and abs(i-visited[i])<=k:
        #         return True
        #     visited[nums[i]]=i
        # return False

        #---Optimal Solution:
        # Using Set
        window=set()
        left=0
        for right in range(len(nums)):
            if right-left > k:
                #shrinking window from left
                window.remove(nums[left])
                left+=1
            if nums[right] in window:
                return True

            window.add(nums[right])
        return False