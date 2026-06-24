# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-recolors-to-get-k-consecutive-black-blocks
# source_path: LeetCode-Solutions-master/Python/minimum-recolors-to-get-k-consecutive-black-blocks.py
# solution_class: Solution
# submission_id: 58ed2cf1426810f8be13883ef0358060e32ec621
# seed: 4008209985

# Time:  O(n)
# Space: O(1)

# sliding window

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        result = k
        curr = 0
        for i, x in enumerate(blocks):
            curr += int(blocks[i] == 'W')
            if i+1-k < 0:
                continue
            result = min(result, curr)
            curr -= int(blocks[i+1-k] == 'W')
        return result