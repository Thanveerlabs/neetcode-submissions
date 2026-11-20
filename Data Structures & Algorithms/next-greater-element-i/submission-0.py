class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []  # Monotonic decreasing stack storing elements from nums2
        
        for num in nums2:
            # Pop elements smaller than current num; current num is their next greater element
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Remaining elements in stack have no next greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        return [next_greater[num] for num in nums1]
        