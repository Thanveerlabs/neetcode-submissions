class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = set("aeiou")
        c = sum(1 for x in s[:k] if x in v)
        ans = c
        for r in range(k, len(s)):
            if s[r] in v:
                c += 1
            if s[r-k] in v:
                c -= 1
            ans = max(ans, c)
        return ans
