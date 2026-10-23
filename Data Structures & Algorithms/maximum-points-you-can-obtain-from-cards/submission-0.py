class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        l = 0
        r = len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total
        while r < len(cardPoints):
            total += cardPoints[l]
            total -= cardPoints[r]
            res = max(res, total)
            l += 1
            r += 1
        return res