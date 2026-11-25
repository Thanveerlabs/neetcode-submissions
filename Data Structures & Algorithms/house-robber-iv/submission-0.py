class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRob(capability):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k
        l, r = min(nums), max(nums)
        while l <= r:
            m = (l + r) // 2
            if canRob(m):
                r = m - 1
            else:
                l = m + 1
        return l        
