from typing import List
from itertools import permutations
import math


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        Returns True if the points form a valid square. A square is defined as a polygon of four points
        whose edges are the same length. The order of the points is arbitrary.
        """
        distance = lambda a, b: math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        pairs = permutations((p1, p2, p3, p4), 2)
        distances = sorted((distance(pair[0], pair[1]) for pair in pairs))

        for distance in distances[:7]:
            if distance != distances[0] or distance == 0:
                return False

        for distance in distances[8:]:
            if distance != distances[8] or distance == 0:
                return False

        return True
