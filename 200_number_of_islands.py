from pprint import pprint


class Solution(object):
    def numIslands(self, grid):
        """
        >>> s = Solution()
        >>> s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
        1

        :type grid: List[List[str]]
        :rtype: int
        """
        EXPLORED = '2'
        LAND = '1'
        SEA = '0'

        def boundary_search(i, j):
            """
            Destructively searches for the boundary of an island.
            :param i:
            :param j:
            :return:
            """
            if not (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1'):
                grid[i][j] = EXPLORED
                boundary_search(i, j + 1)
                boundary_search(i + 1, j)
                boundary_search(i, j - 1)
                boundary_search(i - 1, j)

        def jump_to_end(i, j):
            """
            Returns the first unexplored coordinate past an island.
            :param i:
            :param j:
            :return:
            """
            while j < len(grid[i]):
                if grid[i][j] == SEA:
                    return j
                j += 1
            return j

        island_count = 0
        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[i]):
                if grid[i][j] == LAND:
                    island_count += 1
                    boundary_search(i, j)
                j += 1
            i += 1
        return island_count
