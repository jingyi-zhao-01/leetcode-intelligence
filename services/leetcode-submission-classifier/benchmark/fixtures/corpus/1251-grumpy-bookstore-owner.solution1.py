# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: grumpy-bookstore-owner
# source_path: LeetCode-Solutions-master/Python/grumpy-bookstore-owner.py
# solution_class: Solution
# submission_id: 15109a488243b36e47bc994343300efbf986dc5b
# seed: 3688206551

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        result, max_extra, extra = 0, 0, 0
        for i in xrange(len(customers)):
            result += 0 if grumpy[i] else customers[i]
            extra += customers[i] if grumpy[i] else 0
            if i >= X:
                extra -= customers[i-X] if grumpy[i-X] else 0
            max_extra = max(max_extra, extra)
        return result + max_extra