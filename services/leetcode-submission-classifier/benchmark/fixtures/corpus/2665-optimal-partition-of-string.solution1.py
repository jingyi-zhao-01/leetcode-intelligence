# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: optimal-partition-of-string
# source_path: LeetCode-Solutions-master/Python/optimal-partition-of-string.py
# solution_class: Solution
# submission_id: 490eb6d9705cb0cda64f9e76046d7030be6bf715
# seed: 1670732473

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, left = 1, 0
        lookup = {}
        for i, x in enumerate(s):
            if x in lookup and lookup[x] >= left:
                left = i
                result += 1
            lookup[x] = i
        return result