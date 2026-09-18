class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # array of heights
        # h[i] of ith bar
        # choose any two bars which hold max water
        #2<=len(h)
        s=0
        e=len(heights)-1
        max_water=0
        while s<e:
           total=(e-s)*min(heights[s],heights[e])
           max_water=max(total,max_water)
           if heights[s]<heights[e]:
             s+=1
           else:
             e-=1
        return max_water

