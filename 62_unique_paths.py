class Solution:
    # path_memo = {}
    def uniquePaths(self, m: int, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.uniquePaths(7, 3)
        28
        >>> s.uniquePaths(3, 2)
        3

        Computes the numbers of possible paths the robot can take in an m x n grid.
        A robot may only move down or right.
        :param m: the first dimension of the board
        :param n: the second dimension of the board
        :return:
        """
        # This problem has an optimal substructure:
        # unique_paths(m, n) = unique_paths(m-1, n) + unique_paths(m, n-1)

        # In a 1x1 board, there is exactly one unique path.

        # Compute using Bellman Optimization.

        bellman = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                bellman[i][j] = bellman[i-1][j] + bellman[i][j-1]

        return bellman[-1][-1]