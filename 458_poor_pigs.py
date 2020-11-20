from math import log, floor, ceil


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # If two pigs are used in each iteration, then half of the buckets can be eliminated at a time.
        # => With p pigs, log(buckets, p) is the number of times that we will need to test.
        #    Consider the binary case, where two pigs eliminate half of the buckets in each iteration.
        #
        # So then log(buckets, available_tests) will tell us how many pigs are needed in each round.

        available_tests = floor(minutesToTest / minutesToDie) + 1
        return ceil(log(buckets, available_tests))