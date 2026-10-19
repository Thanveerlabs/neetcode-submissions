class Solution:
    def findInMountainArray(self, target, mountainArr):
        n = mountainArr.length()

        # Find peak
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2

            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m

        peak = l

        # Search left side (ascending)
        l, r = 0, peak

        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)

            if value == target:
                return m
            elif value < target:
                l = m + 1
            else:
                r = m - 1

        # Search right side (descending)
        l, r = peak + 1, n - 1

        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)

            if value == target:
                return m
            elif value > target:
                l = m + 1
            else:
                r = m - 1

        return -1