'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[0:k] = reversed(nums[0:k])
        nums[k:] = reversed(nums[k:])
