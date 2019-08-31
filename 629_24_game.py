from typing import List
from itertools import permutations
from math import isclose


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        """
        >>> s = Solution()
        >>> s.judgePoint24([4, 1, 8, 7])
        True
        >>> s.judgePoint24([1, 2, 1, 2])
        False
        >>> s.judgePoint24([1, 9, 1, 2])
        True

        :param nums:
        :return:
        """

        operators = [
            lambda x, y: x + y,
            lambda x, y: x - y,
            lambda x, y: x * y,
            lambda x, y: x / y if y != 0 else False
        ]

        def evaluate(cards):
            if False in cards:
                return False
            elif len(cards) == 1:
                return isclose(cards[0], 24)

            for c1, c2 in permutations(cards, 2):
                without_pair = list(cards)
                without_pair.remove(c1)
                without_pair.remove(c2)
                if any((evaluate(without_pair + [operator(c1, c2)]) for operator in operators)):
                    return True
            return False

        return evaluate(nums)
