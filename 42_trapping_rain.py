from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it is able to trap after raining.

        :param height:
        :return:
        """
        total_water = 0

        left_boundary = 0
        left_boundary_index = 0

        right_boundary = 0
        right_boundary_index = 0

        
        intermediate_values = []
        for bar in height:
            if bar > left_boundary:
                left_boundary = bar
