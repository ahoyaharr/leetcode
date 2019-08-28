class Solution:
    cache = dict()

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]

        if N <= 1:
            return N

        solution = self.fib(N - 1) + self.fib(N - 2)
        self.cache[N] = solution
        return solution