class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        def kCombos(i,ans,t):
            if t==0:
                result.append(ans)
                return 
            if i>n:
                return
            kCombos(i+1,ans+[i],t-1)
            kCombos(i+1,ans,t)
        kCombos(1,[],k)
        return result