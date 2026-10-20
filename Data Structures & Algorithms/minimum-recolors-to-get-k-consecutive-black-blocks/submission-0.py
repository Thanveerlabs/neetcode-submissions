class Solution:
    def minimumRecolors(self, blocks, k):
        w = blocks[:k].count("W")
        res = w
        l = 0
        for r in range(k, len(blocks)):
            if blocks[r] == "W":
                w += 1

            if blocks[l] == "W":
                w -= 1
            l += 1
            res = min(res, w)
        return res