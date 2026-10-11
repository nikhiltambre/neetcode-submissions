class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def steps(i):
            if i <= 1:
                return 1
            if dp[i]!=-1:
                return dp[i]
            dp[i]= steps(i - 1) + steps(i - 2)
            return dp[i]

        return steps(n)
