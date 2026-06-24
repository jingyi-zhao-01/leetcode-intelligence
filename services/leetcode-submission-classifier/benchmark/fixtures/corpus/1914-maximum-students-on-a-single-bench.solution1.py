# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-students-on-a-single-bench
# source_path: LeetCode-Solutions-master/Python/maximum-students-on-a-single-bench.py
# solution_class: Solution
# submission_id: aef795af917e982a77d817e80be4947f38e086b5
# seed: 1679274316

# Time:  O(n)
# Space: O(n)

import collections


# hash table, unordered set

class Solution(object):
    def maxStudentsOnBench(self, students):
        """
        :type students: List[List[int]]
        :rtype: int
        """
        lookup = collections.defaultdict(set)
        for s, b in students:
            lookup[b].add(s)
        return max(len(x) for x in lookup.itervalues()) if lookup else 0