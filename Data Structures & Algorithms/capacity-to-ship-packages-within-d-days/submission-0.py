class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            daysNeeded = 1
            currWeight = 0
            for w in weights:
                if currWeight + w > m:
                    daysNeeded += 1
                    currWeight = 0
                currWeight += w
            if daysNeeded <= days:
                r = m - 1
            else:
                l = m + 1
        return l