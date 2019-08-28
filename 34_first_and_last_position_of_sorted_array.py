class Solution(object):
    def searchRange(self, nums, target):
        """
        >>> s = Solution()
        >>> s.searchRange([1, 4], 4)
        [1, 1]
        >>> s.searchRange([1, 4], 1)
        [0, 0]
        >>> s.searchRange([1,2,3,3,3,3,4,5,9], 3)
        [2, 5]
        >>> s.searchRange(nums=[5,7,7,8,8,10], target=8)
        [3, 4]
        >>> s.searchRange(nums=[5,7,7,8,8,10], target=6)
        [-1, -1]
        >>> s.searchRange([], 0)
        [-1, -1]
        >>> s.searchRange([1], 1)
        [0, 0]
        >>> s.searchRange([2, 2, 2, 2, 2, 2], 2)
        [0, 5]


        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_left_boundary(left_index=0, right_index=len(nums)-1):
            if left_index > right_index:
                return -1

            if left_index + right_index == 0:
                if nums[0] == target:
                    return 0
                else:
                    return -1

            center = (left_index + right_index) // 2

            if nums[center] == target and (nums[center - 1] < target or center == 0):
                return center
            elif center > 0 and nums[center - 1] >= target:
                # The value(s) we found are too large. Search left
                return find_left_boundary(left_index, center - 1)
            else:
                # The value(s) we found are too small. Search right.
                return find_left_boundary(center + 1, right_index)


        def find_right_boundary(left_index=0, right_index=len(nums)-1):
            if left_index > right_index:
                return -1

            center = (left_index + right_index) // 2

            if center == len(nums) - 1:
                if nums[center] == target:
                    return center
                else:
                    return -1

            if nums[center] == target and nums[center + 1] > target:
                return center
            elif nums[center + 1] <= target:  # The current value is too small, so search right.
                return find_right_boundary(center + 1, right_index)
            else:
                return find_right_boundary(left_index, center - 1)

        left_bound = find_left_boundary()
        right_bound = find_right_boundary()

        return [left_bound, right_bound]