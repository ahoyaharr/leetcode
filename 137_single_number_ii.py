from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
        Find that single one.
        :param nums:
        :return:
        """
        cache = dict()
        for number in nums:
            if number in cache:
                cache[number] -= 1
            else:
                cache[number] = 2

        for number, remaining in cache.items():
            if remaining == 2:
                return number
        return -1