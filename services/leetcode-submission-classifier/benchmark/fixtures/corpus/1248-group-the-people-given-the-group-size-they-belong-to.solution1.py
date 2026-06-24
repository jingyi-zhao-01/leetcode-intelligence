# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: group-the-people-given-the-group-size-they-belong-to
# source_path: LeetCode-Solutions-master/Python/group-the-people-given-the-group-size-they-belong-to.py
# solution_class: Solution
# submission_id: 81346f2c3221fc7fd2b3fed646066ffd4e37d417
# seed: 3308547192

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groups, result = collections.defaultdict(list), []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups.pop(size))
        return result