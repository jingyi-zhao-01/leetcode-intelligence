# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fruit-into-baskets
# source_path: LeetCode-Solutions-master/Python/fruit-into-baskets.py
# solution_class: Solution
# submission_id: 12fd9f417e8955cf0ee4f166981796e89c298845
# seed: 3877724836

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        count = collections.defaultdict(int)
        result, i = 0, 0
        for j, v in enumerate(tree):
            count[v] += 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            result = max(result, j-i+1)
        return result