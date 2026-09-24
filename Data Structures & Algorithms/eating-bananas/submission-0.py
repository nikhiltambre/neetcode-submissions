class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        ans = e
        while s <= e:
            mid = s + (e - s) // 2
            val = sum((math.ceil(p / mid)) for p in piles)
            if val <= h:
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        return ans
