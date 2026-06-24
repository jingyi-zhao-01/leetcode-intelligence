# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-common-subsequence-between-sorted-arrays
# source_path: LeetCode-Solutions-master/Python/longest-common-subsequence-between-sorted-arrays.py
# solution_class: Solution2
# submission_id: e2c5d6a93f6ad6d1c1386d695496031b39540eb0
# seed: 2030356030

# Time:  O(m * n)
# Space: O(l), l is min(len(arr) for arr in arrays)

class Solution2(object):
    def longestCommomSubsequence(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: List[int]
        """
        return [num for num, cnt in collections.Counter(x for arr in arrays for x in arr).iteritems() if cnt == len(arrays)]