# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-longest-valid-obstacle-course-at-each-position
# source_path: LeetCode-Solutions-master/Python/find-the-longest-valid-obstacle-course-at-each-position.py
# solution_class: Solution
# submission_id: 1f711f0de078257ac8df2d018d48df7051427692
# seed: 509521702

# Time:  O(nlogn)
# Space: O(n)

import bisect


# binary search solution

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        result, stk = [], []
        for x in obstacles:
            i = bisect.bisect_right(stk, x)
            result.append(i+1)
            if i == len(stk):
                stk.append(0)
            stk[i] = x
        return result