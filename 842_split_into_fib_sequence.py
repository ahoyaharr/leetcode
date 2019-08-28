from typing import List


class Solution:
    MAXIMUM_VALUE = 2147483647

    def splitIntoFibonacci(self, S: str) -> List[int]:
        """
        >>> s = Solution()
        >>> s.splitIntoFibonacci("11235813")
        [1, 1, 2, 3, 5, 8, 13]
        >>> s.splitIntoFibonacci("123456579")
        [123, 456, 579]
        >>> s.splitIntoFibonacci("112358130")  # The result is empty because there does not exist a fib sequence
        []
        >>> s.splitIntoFibonacci("0123")  # No leading zeroes
        []
        >>> s.splitIntoFibonacci("1011")
        [1, 0, 1, 1]
        >>> s.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")
        []

        The last test case has a "valid" solution of
        [539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511], but
        the maximum allowed value is 2 ** 31 - 1 so it should return [].

        :param S:
        :return:
        """

        def search(string, sequence):
            if len(string) == 0:
                return sequence

            # No leading zeroes allowed, so if the first number if zero we can only use 0.
            if string[0] == '0' and (len(sequence) < 2 or sequence[-2] + sequence[-1] == 0):
                result = search(string[1:], sequence + [0])
                if len(result) > 2:
                    return result
                else:
                    return []

            for i in range(1, len(S)):
                prefix = int(string[:i])

                # Consider no values greater than the maximum value
                if prefix > self.MAXIMUM_VALUE:
                    return []
                suffix = string[i:]

                if len(sequence) < 2 or sequence[-2] + sequence[-1] == prefix:
                    result = search(suffix, sequence + [prefix])
                    if len(result) > 2:
                        return result

            return []

        return search(S, [])
