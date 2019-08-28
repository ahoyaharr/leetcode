from typing import List
from collections import Counter


class Solution:
    solutions = dict()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> {tuple(permutation) for permutation in s.permuteUnique([1,1,2])} == {(1,1,2), (1,2,1), (2,1,1)}
        True
        >>> len(s.permuteUnique([1,1,2]))
        3

        :param nums: 
        :return: 
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [[nums[0]]]

        nums = sorted(nums)
        if tuple(nums) in self.solutions:
            return self.solutions[tuple(nums)]

        permutations = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for child in self.permuteUnique(nums[:i] + nums[i + 1:]):
                for j in range(len(child)):
                    permutation = child[:j] + [nums[i]] + child[j:]
                    permutations.add(tuple(permutation))

        permutations = [list(permutation) for permutation in permutations]
        self.solutions[tuple(nums)] = permutations
        return permutations