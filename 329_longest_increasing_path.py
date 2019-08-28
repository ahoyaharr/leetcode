from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """"
        >>> s = Solution()
        >>> s.longestIncreasingPath([[]])
        0
        >>> s.longestIncreasingPath([[], [], []])
        0
        >>> s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
        4
        >>> s.longestIncreasingPath([[9, 9, 4, 1, 2, 3, 4, 5, 6], [6, 6, 8, 3, 4, 5, 1, 2, 3], [2, 1, 1, 5, 10, 11, 12, 13, 14]])
        8
        >>> s.longestIncreasingPath([[9, 9, 4, 1, 2 , 3, 4, 5, 6],[6, 6, 8, 3, 4, 5, 1, 2, 3], [2, 1, 1, 5, 1, 2, 3, 4, 5]])
        6

        Returns the length of the longest path in a matrix where the value at each step is greater than the value
        at the previous step.

        Runtime: 464 ms, faster than 77.95% of Python3 online submissions for Longest Increasing Path in a Matrix.
        Memory Usage: 18 MB, less than 7.69% of Python3 online submissions for Longest Increasing Path in a Matrix.
        """
        paths = dict()

        def search(i, j):
            if (i, j) in paths:
                return paths[(i, j)]

            values = [0]
            current_value = matrix[i][j]

            if i > 0 and matrix[i - 1][j] > current_value:
                values.append(search(i - 1, j))
            if i < len(matrix) - 1 and matrix[i + 1][j] > current_value:
                values.append(search(i + 1, j))
            if j > 0 and matrix[i][j - 1] > current_value:
                values.append(search(i, j - 1))
            if j < len(matrix[0]) - 1 and matrix[i][j + 1] > current_value:
                values.append(search(i, j + 1))

            result = 1 + max(values)
            paths[(i, j)] = result
            return result

        longest_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                longest_path = max(longest_path, search(i, j))

        return longest_path
