# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-tree-nodes
# source_path: LeetCode-Solutions-master/Python/delete-tree-nodes.py
# solution_class: Solution
# submission_id: 2e72281f266c92ae9652800c0751ba656fb41cb4
# seed: 3573274080

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        def dfs(value, children, x):
            total, count = value[x], 1
            for y in children[x]:
                t, c = dfs(value, children, y)
                total += t
                count += c if t else 0
            return total, count if total else 0

        children = collections.defaultdict(list)
        for i, p in enumerate(parent):
            if i:
                children[p].append(i)
        return dfs(value, children, 0)[1]