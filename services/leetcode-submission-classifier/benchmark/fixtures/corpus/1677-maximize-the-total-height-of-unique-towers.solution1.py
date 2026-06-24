# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-total-height-of-unique-towers
# source_path: LeetCode-Solutions-master/Python/maximize-the-total-height-of-unique-towers.py
# solution_class: Solution
# submission_id: be3eb57248f65d33faa781ef67966ef9c56888cf
# seed: 3155472790

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        """
        :type maximumHeight: List[int]
        :rtype: int
        """
        maximumHeight.sort()
        result, prev = 0, maximumHeight[-1]+1
        for x in reversed(maximumHeight):
            prev = min(x, prev-1)
            if prev == 0:
                return -1
            result += prev
        return result