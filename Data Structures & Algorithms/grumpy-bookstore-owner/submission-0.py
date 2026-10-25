class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        total = 0
        window = 0
        res = 0
        for r in range(len(customers)):
            if grumpy[r] == 0:
                total += customers[r]
            else:
                window += customers[r]
            if r >= minutes:
                if grumpy[r - minutes]:
                    window -= customers[r - minutes]
            res = max(res, window)
        return total + res