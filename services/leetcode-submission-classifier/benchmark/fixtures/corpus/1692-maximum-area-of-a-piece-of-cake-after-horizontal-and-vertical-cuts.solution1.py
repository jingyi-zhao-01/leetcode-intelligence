# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
# source_path: LeetCode-Solutions-master/Python/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts.py
# solution_class: Solution
# submission_id: ebed5f520a940cb0cbba5c91b6be104c1b445aec
# seed: 3537222885

# Time:  O(hlogh + wlogw)
# Space: O(1)

class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        def max_len(l, cuts):
            cuts.sort()
            l = max(cuts[0]-0, l-cuts[-1])
            for i in xrange(1, len(cuts)):
                l = max(l, cuts[i]-cuts[i-1])
            return l

        MOD = 10**9+7
        return max_len(h, horizontalCuts) * max_len(w, verticalCuts) % MOD