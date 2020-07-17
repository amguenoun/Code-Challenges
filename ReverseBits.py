'''
Reverse bits of a given 32 bits unsigned integer.
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        return(int(bin(n)[2:].zfill(32)[::-1], 2))
