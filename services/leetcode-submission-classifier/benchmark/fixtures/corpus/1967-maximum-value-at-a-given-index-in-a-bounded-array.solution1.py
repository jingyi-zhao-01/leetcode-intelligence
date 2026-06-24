# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-value-at-a-given-index-in-a-bounded-array
# source_path: LeetCode-Solutions-master/Python/maximum-value-at-a-given-index-in-a-bounded-array.py
# solution_class: Solution
# submission_id: 7989111bc00f6c4a525005d7d6340f8b4f58709e
# seed: 2305120891

# Time:  O(logm)
# Space: O(1)

class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def check(n, index, maxSum, x):
            y = max(x-index, 0)
            total = (x+y)*(x-y+1)//2
            y = max(x-((n-1)-index), 0)
            total += (x+y)*(x-y+1)//2
            return total-x <= maxSum

        maxSum -= n
        left, right = 0, maxSum
        while left <= right:
            mid = left + (right-left)//2
            if not check(n, index, maxSum, mid):
                right = mid-1
            else:
                left = mid+1
        return 1+right