class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            coins = m * (m + 1) // 2
            if coins <= n:
                l = m + 1
            else:
                r = m - 1
        return r
        