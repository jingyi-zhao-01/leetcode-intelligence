# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: mirror-reflection
# source_path: LeetCode-Solutions-master/Python/mirror-reflection.py
# solution_class: Solution
# submission_id: bb7e1ea984dd214d5f64f16eadd016bdd3ee28b2
# seed: 1038356980

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        # explanation commented in the following solution
        return 2 if (p & -p) > (q & -q) else 0 if (p & -p) < (q & -q) else 1