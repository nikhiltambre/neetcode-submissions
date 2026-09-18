class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        e = len(height) - 1
        max_left = height[s]
        max_right = height[e]
        res=0
        while s<e:
            if max_left<max_right:
               s+=1 
               max_left=max(max_left,height[s])
               res+=max_left-height[s]
            else:
                e-=1
                max_right=max(max_right,height[e])
                res+=max_right-height[e]
        return res
      
