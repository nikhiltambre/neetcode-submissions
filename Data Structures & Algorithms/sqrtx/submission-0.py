class Solution:
    def mySqrt(self, x: int) -> int:
       s=1
       e=x
       while s<=e:
        mid=s+(e-s)//2
        square=mid*mid
        if square==x:
            return mid
        elif square<x:
            s=mid+1
        else :
            e=mid-1
       
       return s-1
