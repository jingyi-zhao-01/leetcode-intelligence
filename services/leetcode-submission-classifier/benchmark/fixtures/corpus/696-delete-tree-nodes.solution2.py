# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-tree-nodes
# source_path: LeetCode-Solutions-master/Python/delete-tree-nodes.py
# solution_class: Solution2
# submission_id: 76abc10c852df27fa400433f6be85f4cc75cea53
# seed: 893771760

# Time:  O(n)
# Space: O(n)

import collections

class Solution2(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        # assuming parent[i] < i for all i > 0
        result = [1]*nodes
        for i in reversed(xrange(1, nodes)):
            value[parent[i]] += value[i]
            result[parent[i]] += result[i] if value[i] else 0
        return result[0]