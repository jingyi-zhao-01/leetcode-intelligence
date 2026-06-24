# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: diet-plan-performance
# source_path: LeetCode-Solutions-master/Python/diet-plan-performance.py
# solution_class: Solution
# submission_id: d4fd2d5c44de17025842b4f7e3f156637e30f89e
# seed: 523322943

# Time:  O(n)
# Space: O(1)

import itertools

class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        total = sum(itertools.islice(calories, 0, k))
        result = int(total > upper)-int(total < lower)
        for i in xrange(k, len(calories)):
            total += calories[i]-calories[i-k]
            result += int(total > upper)-int(total < lower)
        return result