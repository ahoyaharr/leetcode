from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        """
        Runtime: 232 ms, faster than 94.45% of Python3 online submissions for N-Repeated Element in Size 2N Array.
        Memory Usage: 14.8 MB, less than 6.12% of Python3 online submissions for N-Repeated Element in Size 2N Array.
        """
        seen = set()

        for number in A:
            if number in seen:
                return number
            seen.add(number)

        return -1
