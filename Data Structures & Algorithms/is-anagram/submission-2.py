class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(1) space since it stores 26 characters
        if len(s)!=len(t):
            return False
        temp=dict()
        #store frequency 
        for ch in s:
            temp[ch]=temp.get(ch,0)+1
        #lookup
        for ch in t:
            if ch not in temp or temp[ch]==0:
                return False
            temp[ch]-=1
                
        return True