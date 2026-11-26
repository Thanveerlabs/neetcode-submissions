class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(k):
            removed = set(removable[:k])
            j = 0
            for i in range(len(s)):
                if i in removed:
                    continue
                if j < len(p) and s[i] == p[j]:
                    j += 1
            return j == len(p)
        l, r = 0, len(removable)
        while l <= r:
            m = (l + r) // 2
            if isSubsequence(m):
                l = m + 1
            else:
                r = m - 1
        return r