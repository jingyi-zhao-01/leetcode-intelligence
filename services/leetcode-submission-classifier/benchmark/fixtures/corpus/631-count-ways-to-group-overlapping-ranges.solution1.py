# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-ways-to-group-overlapping-ranges
# source_path: LeetCode-Solutions-master/Python/count-ways-to-group-overlapping-ranges.py
# solution_class: Solution
# submission_id: c5172cc51c3e981a5f8a8929d132d71dea089d66
# seed: 1713552794

# Time:  O(nlogn)
# Space: O(1)

# sort, array

class Solution(object):
    def countWays(self, ranges):
        """
        :type ranges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7

        ranges.sort()
        cnt = 0
        curr = float("-inf")
        for l, r in ranges:
            if l > curr:
                cnt += 1
            curr = max(curr, r)
        return pow(2, cnt, MOD)