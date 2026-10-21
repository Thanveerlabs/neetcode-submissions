class Solution:
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
            res = max(res, r - l + 1)
        return res