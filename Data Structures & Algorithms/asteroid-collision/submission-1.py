class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
         #asteroid int
         # index->relative position
         # value->size , sign->direction
         #+ve -> right , -ve -> left
         # speed same
         #smaller explode,same size-> both explode 
         # same direction never meet
         ans=deque()
         for a in asteroids:
            destroyed=False
            while ans and a<0 and ans[-1]>0: 
                if abs(a)==abs(ans[-1]):
                    ans.pop()
                    destroyed=True
                    break
                elif(abs(a)>abs(ans[-1]) ):
                    ans.pop()
                else:
                    destroyed=True
                    break
                   
            
            if not destroyed:
                ans.append(a)
         return list(ans)
    