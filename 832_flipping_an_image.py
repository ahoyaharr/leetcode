from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def invert(bit):
            return abs(bit - 1)  # 1 -> 0; 0 -> -1 -> 1

        return [[invert(bit) for bit in row[::-1]] for row in A]