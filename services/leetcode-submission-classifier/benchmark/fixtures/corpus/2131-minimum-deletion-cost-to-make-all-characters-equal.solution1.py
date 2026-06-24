# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-deletion-cost-to-make-all-characters-equal
# source_path: LeetCode-Solutions-master/Python/minimum-deletion-cost-to-make-all-characters-equal.py
# solution_class: Solution
# submission_id: bc5390050d4fdd0fc1590c48bd40177f214649c2
# seed: 281599989

# Time:  O(n + 26)
# Space: O(26)

# freq table

class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        total = sum(cost)
        cnt = [0]*26
        for i in xrange(len(s)):
            cnt[ord(s[i])-ord('a')] += cost[i]
        return total-max(cnt)