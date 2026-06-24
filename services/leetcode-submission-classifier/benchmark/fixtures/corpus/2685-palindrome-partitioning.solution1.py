# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-partitioning
# source_path: LeetCode-Solutions-master/Python/palindrome-partitioning.py
# solution_class: Solution
# submission_id: 27ceb132ea34efdba15405244ae5663e30eb325c
# seed: 2959401428

# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        is_palindrome = [[False] * len(s) for i in xrange(len(s))]
        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                is_palindrome[i][j] = s[i] == s[j] and ((j - i < 2) or is_palindrome[i + 1][j - 1])

        sub_partition = [[] for _ in xrange(len(s))]
        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                if is_palindrome[i][j]:
                    if j + 1 < len(s):
                        for p in sub_partition[j + 1]:
                            sub_partition[i].append([s[i:j + 1]] + p)
                    else:
                        sub_partition[i].append([s[i:j + 1]])

        return sub_partition[0]