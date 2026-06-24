# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-wonderful-substrings
# source_path: LeetCode-Solutions-master/Python/number-of-wonderful-substrings.py
# solution_class: Solution
# submission_id: a28ab7f7268b460a41977f70b8c51285602637ac
# seed: 2002127012

# Time:  O(n)
# Space: O(2^10)

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        ALPHABET_SIZE = 10
        count = [0]*(2**ALPHABET_SIZE)
        count[0] = 1
        result = curr = 0
        for c in word:
            curr ^= 1<<(ord(c)-ord('a'))
            result += count[curr]
            result += sum(count[curr^(1<<i)] for i in xrange(ALPHABET_SIZE))
            count[curr] += 1
        return result