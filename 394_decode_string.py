class Solution(object):
    def decodeString(self, s):
        """
        >>> s = Solution()
        >>> s.decodeString('100[leetcode]')
        'leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode'
        >>> s.decodeString('3[z]2[2[y]pq4[2[jk]e1[f]]]ef')
        'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef'
        >>> s.decodeString('abc')
        'abc'
        >>> s.decodeString('')
        ''
        >>> s.decodeString('3[a]2[bc]')
        'aaabcbc'
        >>> s.decodeString('3[a2[c]]')
        'accaccacc'
        >>> s.decodeString('2[abc]3[cd]ef')
        'abcabccdcdcdef'
        >>> s.decodeString('3[a2[c]]3[a2[c]]zz')
        'accaccaccaccaccacczz'

        :type s: str
        :rtype: str
        """
        # Compute the boundaries of the token.
        left_index, right_index = s.find('['), s.find(']')
        depth = s[:right_index].count('[')
        while depth - 1 > 0: # We want to find the ']' that is of equal depth to the first '['
            old_right_index = right_index
            right_index += s[right_index + 1:].index(']') + 1  # Move the right index to the next ']' that we find
            # Each time we find a '[', the depth increases by 1
            # Each time we find a ']', the depth decreases by 1
            depth += s[old_right_index + 1:right_index].count('[') - 1  # Adjust the depth

        if left_index == -1 or right_index == -1:  # The only thing that remains are characters
            return s
        else:  # We found a token and need to break it into pieces to evaluate
            # Get the number of times the token should be repeated, e.g. 100 for '100[a]'
            repeat_count = ''
            i = 1
            while s[left_index - i].isnumeric():
                repeat_count = s[left_index - i] + repeat_count
                i += 1

            zeroth_token = s[:left_index - len(repeat_count)]  # Prefix characters, e.g. 'A' in the case of 'A10[B]'
            first_token = s[left_index + 1:right_index]  # The current token
            remainder = s[right_index + 1:]  # All of the remaining tokens, e.g. '5[B]C' in the case of '10[A]5[B]C'
            # print('recursing. result will be = {0} || {1} * {2} || {3}'.format(zeroth_token, repeat_count, first_token, remainder))
            return self.decodeString(zeroth_token) + \
                   int(repeat_count) * self.decodeString(first_token) + \
                   self.decodeString(remainder)
