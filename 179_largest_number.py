from math import log10


class Solution(object):
    def largestNumber(self, nums):
        """
        >>> s = Solution()
        >>> s.largestNumber([3,30,34,5,9])
        '9534330'
        >>> s.largestNumber([20,1])
        '201'
        >>> s.largestNumber([1,2,3,4,5,6,7,8,9,0])
        '9876543210'
        >>> s.largestNumber([121,12])
        '12121'
        >>> s.largestNumber([0,0])
        '0'

        Given a list of non negative integers,
        arrange them such that they form the largest number.
        :type nums: List[int]
        :rtype: str
        """

        def safe_log10(x):
            if x == 0:
                return 1
            else:
                return int(log10(x))

        def compare(a):
            """
            Pads a with it's first digit until it is the same number of digits as the largest number in the set.
            Numbers should be compared by their most significant digit. If there is a tie, the comparisons should
            continue until a number runs out of digits.
            Given two numbers which tie until one number runs out of digits, the number which runs out of digits is
            the larger value because it frees up a digit.

            Example: 34 v. 30 - pick 34
            Example: 9 v 99 - pick 9
            Example: 9 v 98 - pick 9
            :param a: an integer
            :return:
            """
            lg10_a = int(safe_log10(a))
            first_digit = a // 10 ** lg10_a
            a = a * 10 ** (maximum_digits - lg10_a)
            for i in range(maximum_digits - lg10_a):
                a += first_digit * (10 ** i)
            return a, maximum_digits - lg10_a  # Break the tie by selecting the smaller of the two

        if max(nums) == 0:
            return '0'

        # The number of digits in the largest number
        maximum_digits = int(safe_log10(max(nums, key=lambda x: int(safe_log10(x)))))
        nums = sorted(nums, key=compare, reverse=True)
        return ''.join((str(number) for number in nums))
