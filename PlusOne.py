'''
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:

Input: digits = [0]
Output: [1]

'''


class Solution:
    def plusOne(self, A):
        if len(A) == 0:
            return A

        A.reverse()
        cache = 1
        for i in range(len(A)):
            val = A[i] + cache
            A[i] = val % 10
            cache = val // 10

        if cache:
            A.append(cache)
        while(A[-1] == 0):
            A.pop()

        A.reverse()
        return A
