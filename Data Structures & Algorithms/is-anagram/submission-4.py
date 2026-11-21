class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        temp=dict()
        for char in s:
            #getting the character if exists(if not then 0)
            temp[char]=temp.get(char,0)+1
        for ch in t:
            if  ch not in temp or temp[ch]==0:
                return False
            temp[ch]-=1
        return True