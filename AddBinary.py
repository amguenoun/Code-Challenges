'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    Each string consists only of '0' or '1' characters.
    1 <= a.length, b.length <= 10^4
    Each string is either "0" or doesn't contain any leading zero.
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                carry += int(a[i]) + int(b[j])
                i, j = i-1, j-1
            elif i >= 0:
                carry += int(a[i])
                i -= 1
            else:
                carry += int(b[j])
                j -= 1

            c = str(carry % 2) + c
            carry //= 2

        return "1" + c if carry else c
