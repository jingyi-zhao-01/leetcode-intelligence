# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-make-x-and-y-equal
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-make-x-and-y-equal.py
# solution_class: Solution
# submission_id: 9004c46b004faf67c0b79a8135681b3a4009bd33
# seed: 208889252

# Time:  O(x)
# Space: O(x)

# memoization

class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def memoization(x):
            if y >= x:
                return y-x
            if x not in lookup:
                lookup[x] = min(x-y, min(min(x%d, d-x%d)+memoization(x//d+int(d-x%d < x%d))+1 for d in (5, 11)))
            return lookup[x]
    
        lookup = {}
        return memoization(x)