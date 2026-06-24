# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-unequal-adjacent-groups-subsequence-i
# source_path: LeetCode-Solutions-master/Python/longest-unequal-adjacent-groups-subsequence-i.py
# solution_class: Solution
# submission_id: 6e256d7099bdba14cfac7e1df6c1949e56f0782c
# seed: 2842489646

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        """
        :type n: int
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        return [words[i] for i in xrange(n) if i == 0 or groups[i-1] != groups[i]]