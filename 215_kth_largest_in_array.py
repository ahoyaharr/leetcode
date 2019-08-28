from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> s.findKthLargest([3,2,1,5,6,4], 2)
        5
        >>> s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
        4

        :param nums: an unsorted list of values
        :param k: kth largest in sorted order (not distinct value) (e.g., k=1 returns the largest value)
        """
        return sorted(nums)[-k]