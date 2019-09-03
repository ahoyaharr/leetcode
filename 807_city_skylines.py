from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        Runtime: 88 ms, faster than 51.60% of Python3 online submissions for Max Increase to Keep City Skyline.
        Memory Usage: 13.9 MB, less than 5.00% of Python3 online submissions for Max Increase to Keep City Skyline.
        :param grid:
        :return:
        """
        HORIZONTAL_LENGTH, VERTICAL_LENGTH = len(grid), len(grid[0])
        horizontal_maximums = [0] * HORIZONTAL_LENGTH
        vertical_maximums = [0] * VERTICAL_LENGTH

        for i in range(HORIZONTAL_LENGTH):
            for j in range(VERTICAL_LENGTH):
                horizontal_maximums[i] = max(horizontal_maximums[i], grid[i][j])
                vertical_maximums[j] = max(vertical_maximums[j], grid[i][j])

        total = 0
        for i in range(HORIZONTAL_LENGTH):
            for j in range(VERTICAL_LENGTH):
                total += min(horizontal_maximums[i], vertical_maximums[j]) - grid[i][j]

        return total
