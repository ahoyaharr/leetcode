from typing import List
from functools import reduce


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        >>> s = Solution()
        >>> s.wordBreak(s = "leetcode", wordDict = ["leet", "code"])
        True
        >>> s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"])
        True
        >>> s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])
        False
        >>> s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
        False

        Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can
        be segmented into a space-separated sequence of one or more dictionary words.

        Runtime: 32 ms, faster than 99.49% of Python3 online submissions for Word Break.
        Memory Usage: 13.7 MB, less than 5.55% of Python3 online submissions for Word Break.

        :param s:
        :param wordDict:
        :return:
        """
        memo = dict()

        def search(substring):
            if substring == '':
                return True

            if substring in memo:
                return memo[substring]

            memo[substring] = False
            for word in wordDict:
                if substring.find(word) == 0 and search(substring[len(word):]):
                    memo[substring] = True
                    break

            return memo[substring]

        return search(s)
