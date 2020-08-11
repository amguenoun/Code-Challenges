'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
'''


class Solution:
    def addDigits(self, num: int) -> int:
        l = list(str(num))
        l = list(map(int, l))
        num = sum(l)
        if len(str(num)) > 1:
            num = self.addDigits(num)
        return num
