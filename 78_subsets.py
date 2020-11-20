from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given a list of distinct integers, return all possible subsets (the power set).
        :param nums: A list of distinct integers.
        :return:
        """
        # A power set of n distinct values has a cardinality of 2 ** n.
        cardinality = 2 ** len(nums)
        power_set = [list() for _ in range(cardinality)]
        # There is a bijection between members of the power set and natural numbers.
        # Interpret the natural number as a bit string. If the 0 <= k <= len(nums) bit of the bit string is 1,
        # then the set contains the kth distinct value.
        for value in range(cardinality):
            subset_bits = bin(value)[2:].zfill(len(nums))  # The integer represented as a bit string, with left padding.
            for i in range(len(subset_bits)):
                if subset_bits[i] == '1':
                    power_set[value].append(nums[i])

        return power_set

print(Solution().subsets(nums = [1,2,3]))