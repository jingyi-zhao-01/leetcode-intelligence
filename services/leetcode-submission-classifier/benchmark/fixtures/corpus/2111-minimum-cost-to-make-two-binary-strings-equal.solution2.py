# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-make-two-binary-strings-equal
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-make-two-binary-strings-equal.py
# solution_class: Solution2
# submission_id: f39bc6dc09b7f88811d2f025d3551ab53915bbd9
# seed: 3505055160

# Time:  O(n)
# Space: O(1)

# math

class Solution2(object):
    def minimumCost(self, s, t, flipCost, swapCost, crossCost):
        """
        :type s: str
        :type t: str
        :type flipCost: int
        :type swapCost: int
        :type crossCost: int
        :rtype: int
        """
        cnt = [0]*2
        for i in xrange(len(s)):
            if s[i] == t[i]:
                continue
            cnt[ord(s[i])-ord('0')] += 1
        mn, mx = min(cnt[0], cnt[1]), max(cnt[0], cnt[1])
        q, r = divmod(mx-mn, 2)
        return min((mx+mn)*flipCost, mn*swapCost+(mx-mn)*flipCost, mn*swapCost+q*(crossCost+swapCost)+r*flipCost)