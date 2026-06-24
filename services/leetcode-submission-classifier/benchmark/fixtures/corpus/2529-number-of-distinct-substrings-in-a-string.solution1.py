# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-distinct-substrings-in-a-string
# source_path: LeetCode-Solutions-master/Python/number-of-distinct-substrings-in-a-string.py
# solution_class: Solution
# submission_id: 93fd3fa0e712feeeedeb1ff8b2eb0c64aaece882
# seed: 1967272857

# Time:  O(n^2)
# Space: O(t), t is the number of trie nodes

class Solution(object):
    def countDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        trie = {}
        for i in xrange(len(s)):
            curr = trie
            for j in xrange(i, len(s)):
                if s[j] not in curr:
                    count += 1
                    curr[s[j]] = {}
                curr = curr[s[j]]
        return count