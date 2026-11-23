class Solution:

  def maxAscendingSum(self, nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]

    for i in range(1, len(nums)):
      # Strictly ascending: extend the current subarray sum
      if nums[i] > nums[i - 1]:
        curr_sum += nums[i]
      # Otherwise, start a new ascending subarray at nums[i]
      else:
        curr_sum = nums[i]

      if curr_sum > max_sum:
        max_sum = curr_sum

    return max_sum
    
        