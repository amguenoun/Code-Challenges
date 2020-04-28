'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
'''


class Solution:
    def reverse(self, x: int) -> int:
        negative = 1
        if x < 0:
            negative = -1
            x *= -1

        numStr = str(x)
        newStr = ""

        for i in range(1, len(numStr) + 1):
            newStr += numStr[-i]

        if int(newStr) > 2**31 - 1:
            return 0

        return int(newStr) * negative
