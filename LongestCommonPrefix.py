'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        commonPrefix = strs[0]

        for word in strs:
            sharedPrefix = ''
            for j in range(len(word)):
                if j < len(word) and j < len(commonPrefix) and word[j] == commonPrefix[j]:
                    sharedPrefix += word[j]
                else:
                    break
            if len(sharedPrefix) < len(commonPrefix):
                commonPrefix = sharedPrefix

        return commonPrefix
