class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        window = set()
        maxlen = 0
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1

            maxlen = max(maxlen, R - L + 1)
            window.add(s[R])
        return maxlen
