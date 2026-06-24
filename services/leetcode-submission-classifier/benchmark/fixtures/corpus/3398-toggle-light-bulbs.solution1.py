# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: toggle-light-bulbs
# source_path: LeetCode-Solutions-master/Python/toggle-light-bulbs.py
# solution_class: Solution
# submission_id: ad0c6f574abe0f1b08a4c9ea069400f19a55c618
# seed: 3914263512

# Time:  O(n + r)
# Space: O(r)

# freq table, counting sort

class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        mx = max(bulbs)
        cnt = [0]*(mx+1)
        for x in bulbs:
            cnt[x] ^= 1
        return [k for k in xrange(1, mx+1) if cnt[k]]