# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: removing-minimum-number-of-magic-beans
# source_path: LeetCode-Solutions-master/Python/removing-minimum-number-of-magic-beans.py
# solution_class: Solution
# submission_id: 5f6a4fce9804c9acb73d3444009250f3ea144c54
# seed: 1191561299

# Time:  O(nlogn)
# Space: O(1)

# math

class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans.sort()
        return sum(beans) - max(x*(len(beans)-i)for i, x in enumerate(beans))