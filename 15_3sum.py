from collections import Counter


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_counter = Counter(nums)

        sum_list = []

        if 0 in nums_counter and nums_counter[0] > 2:
            sum_list.append([0, 0, 0])

        nums_neg = [k for k in nums_counter.keys() if k < 0]
        nums_pos = [k for k in nums_counter.keys() if k >= 0]

        for n in nums_neg:
            for p in nums_pos:
                target = -n - p
                if target in nums_counter:
                    if target in [n, p] and nums_counter.get(target) >= 2:
                        sum_list.append([n, p, target])

                    if target > p or target < n:
                        sum_list.append([n, p, target])

        return sum_list
