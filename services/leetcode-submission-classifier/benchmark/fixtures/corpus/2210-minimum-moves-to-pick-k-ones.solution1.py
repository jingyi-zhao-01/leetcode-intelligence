# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-pick-k-ones
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-pick-k-ones.py
# solution_class: Solution
# submission_id: 2cf66f4e5d66a19e75a7445aa6db3250cef2dffa
# seed: 3465358971

# Time:  O(n)
# Space: O(n)

# prefix sum, greedy

class Solution(object):
    def minimumMoves(self, nums, k, maxChanges):
        """
        :type nums: List[int]
        :type k: int
        :type maxChanges: int
        :rtype: int
        """
        idxs = [i for i, x in enumerate(nums) if x]
        prefix = [0]*(len(idxs)+1)
        for i in xrange(len(idxs)):
            prefix[i+1] = prefix[i]+idxs[i]
        result = float("inf")
        cnt = max(k-maxChanges, 0)
        for l in xrange(cnt, min(cnt+3, k, len(idxs))+1):
            cnt1 = (k-l)*2
            for i in xrange(len(idxs)-l+1):
                cnt2 = (prefix[(i+l-1)+1]-prefix[(i+l-1)-(l//2-1)])-(prefix[(i+(l//2-1))+1]-prefix[i])
                result = min(result, cnt2+cnt1)
        return result