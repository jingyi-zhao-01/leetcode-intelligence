# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reducing-dishes
# source_path: LeetCode-Solutions-master/Python/reducing-dishes.py
# solution_class: Solution
# submission_id: a666c7e3590e9e4520d513c793acf0bbcbde5fd2
# seed: 2793093521

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse=True)
        result, curr = 0, 0
        for x in satisfaction:
            curr += x
            if curr <= 0:
                break
            result += curr
        return result