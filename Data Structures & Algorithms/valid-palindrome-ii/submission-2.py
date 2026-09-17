class Solution:
    def isPalindrome(self,sub:str)->bool:
        return sub==sub[::-1]
            
    def validPalindrome(self, s: str) -> bool:
        start=0
        end=len(s)-1
        result=False
        while start<end:
            if s[start]!=s[end]:
                if self.isPalindrome(s[start+1:end+1]) or self.isPalindrome(s[start:end]):
                    return True
                else:
                    return False
             
            start+=1
            end-=1

        return True
         