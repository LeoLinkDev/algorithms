"""
File: app.py
Problem: 2855. Minimum Right Shifts to Sort the Array
Link: https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/
Difficulty: Easy
Topics: Array

Description:
    Given a 0-indexed array 'nums' of length 'n' containing distinct positive 
    integers, return the minimum number of right shifts required to sort 'nums' 
    and -1 if this is not possible.

Algorithm / Pattern:
    Linear Scan / Rotation Pivot Detection (Circular Monotonicity Check)
    - Identify the single drop point where nums[i] < nums[i - 1].
    - Verify no other drops exist and the wrap-around boundary (nums[-1] < nums[0]) holds.

Complexity:
    Time:  O(n) - Single pass through the array.
    Space: O(1) - Constant extra space used.
"""
from typing import List

class ShiftRight:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        drop_idx = -1
        
        for i in range(1, n):
            '''
            Rotation Pivot Detection (or Inflection Point Finding): 
            Finding the exact index where a rotated sorted array wraps around—specifically 
            where the monotonic property breaks (nums[i] < nums[i - 1]).
            '''
            if nums[i] < nums[i - 1]:
                # If we find more than one drop, it cannot be sorted by shifting
                if drop_idx != -1:
                    return -1
                drop_idx = i
                
        # If no drop was found, the array is already sorted
        if drop_idx == -1:
            return 0
            
        # After wrapping around, the last element must be smaller than the first element
        if nums[-1] > nums[0]:
            return -1
            
        return n - drop_idx