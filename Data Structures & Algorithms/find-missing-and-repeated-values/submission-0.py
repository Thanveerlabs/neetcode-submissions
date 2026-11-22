from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n

        expected_sum = N * (N + 1) // 2
        expected_sq_sum = N * (N + 1) * (2 * N + 1) // 6

        actual_sum = 0
        actual_sq_sum = 0

        for row in grid:
            for val in row:
                actual_sum += val
                actual_sq_sum += val * val

        # diff1 = a - b
        diff1 = actual_sum - expected_sum
        # diff2 = a^2 - b^2 = (a - b)(a + b)
        diff2 = actual_sq_sum - expected_sq_sum

        # sum_ab = a + b
        sum_ab = diff2 // diff1

        repeated = (diff1 + sum_ab) // 2
        missing = repeated - diff1

        return [repeated, missing]