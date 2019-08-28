class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Counts the number of primes in the range (0, n) using the Sieve of Eratosthenes

        >>> soln = Solution()
        >>> soln.countPrimes(10)
        4
        >>> soln.countPrimes(0)
        0
        >>> soln.countPrimes(1)
        0
        >>> soln.countPrimes(2)  # n is not inclusive
        0
        >>> soln.countPrimes(3)
        1
        >>> soln.countPrimes(34563)
        3692
        >>> soln.countPrimes(499979)
        41537
        >>> soln.countPrimes(1500000)
        114155
        """
        #  Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
        numbers = [i for i in range(n)]

        prime_marker = 2  # Set the marker to the value of the smallest prime number, 2
        while prime_marker is not None and prime_marker ** 2 < n:
            #  Mark all of the multiples of prime_marker that have a coefficient > 1 (2p, 3p, ..., but not p itself)
            for i in range((n - prime_marker ** 2) // prime_marker + 1):
                try:
                    numbers[prime_marker ** 2 + i * prime_marker] = False
                except IndexError:
                    break

            try:  # If a number greater than prime_marker exists, set prime_marker to be that value.
                prime_marker = next(filter(lambda x: bool(x) is True, numbers[prime_marker + 1:]))
            except StopIteration:  # If there was no such number, stop.
                prime_marker = None

        # All unmarked numbers in the range [2, n] are primes. Return the length of a list of these numbers.
        return len([x for x in numbers[2:] if bool(x)])