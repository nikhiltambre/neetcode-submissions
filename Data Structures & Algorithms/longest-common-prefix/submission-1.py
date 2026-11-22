class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
         
        ans=""
        n = min(len(strs[0]),len(strs[1]))
        for i in range(n):
            if strs[0][i]==strs[1][i]:
                ans+=strs[0][i]
            else: 
                break

        for s in strs[2:]:
            while not  s.startswith(ans):
               #trim until you find ans 
               ans=ans[:-1]
               if not ans:
                return ""
        return ans
            

