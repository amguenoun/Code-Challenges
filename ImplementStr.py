'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # get the length of the needle
        needle_length = len(needle)

        # if empty string, return 0
        if not needle:
            return 0

        # loop through each character in string
        for i in range(len(haystack)):

            # define each guess is the length of the needle
            guess = haystack[i:i+needle_length]

            # compare the guess to the needle, return index if they are identical
            if guess == needle:
                return i

        # return -1 if no guess matches the needle
        return -1
