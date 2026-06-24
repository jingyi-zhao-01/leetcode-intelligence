# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-capacity-box
# source_path: LeetCode-Solutions-master/Python/minimum-capacity-box.py
# solution_class: Solution
# submission_id: 2447356cc78084718bcfc98bbd773aec129e3fa5
# seed: 4240271736

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        result = (float("inf"), -1)
        for i, x in enumerate(capacity):
            if x >= itemSize:
                result = min(result, (x, i))
        return result[1]