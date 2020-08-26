'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true

Example 2:

Input: 5
Output: false

'''


def isPowerOfFour(self, num: int) -> bool:
    return num > 0 and log(num, 4).is_integer()
