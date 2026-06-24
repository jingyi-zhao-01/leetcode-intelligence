# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-smallest-number-in-multiplication-table
# source_path: LeetCode-Solutions-master/Python/kth-smallest-number-in-multiplication-table.py
# solution_class: Solution
# submission_id: ee34bff929d1e48182052100760d04b69bedf039
# seed: 3696384930

# Time:  O(m * log(m * n))
# Space: O(1)

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(target, m, n):
            return sum(min(target//i, n) for i in xrange(1, m+1))

        left, right = 1, m*n
        while left <= right:
            mid = left + (right-left)/2
            if count(mid, m, n) >= k:
                right = mid-1
            else:
                left = mid+1
        return left