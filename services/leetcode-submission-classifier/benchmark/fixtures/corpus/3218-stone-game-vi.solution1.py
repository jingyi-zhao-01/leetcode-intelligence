# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stone-game-vi
# source_path: LeetCode-Solutions-master/Python/stone-game-vi.py
# solution_class: Solution
# submission_id: e64c9f970321bfbea595ffb26e4da918710e0d56
# seed: 1001414577

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        sorted_vals = sorted(((a, b) for a, b in zip(aliceValues, bobValues)), key=sum, reverse=True)
        return cmp(sum(a for a, _ in sorted_vals[::2]), sum(b for _, b in sorted_vals[1::2]))