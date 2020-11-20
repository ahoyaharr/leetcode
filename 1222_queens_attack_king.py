from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def valid_attack(queen):
            # Return True if the queen is on a diagonal, vertical, or horizontal from the king.
            # Does not check collisions.
            return queen[0] == king[0] or queen[1] == king[1] or abs(queen[0] - king[0]) == abs(queen[1] - king[1])

        board = [[True] * 8] * 8

        # Iterate in a spiral, radiating out from the king. When a queen is found, mark the bad positions. 