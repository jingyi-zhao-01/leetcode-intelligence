# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-n-unique-integers-sum-up-to-zero
# source_path: LeetCode-Solutions-master/Python/find-n-unique-integers-sum-up-to-zero.py
# solution_class: Solution
# submission_id: b809fed518e52817eaf09dd5428411ec20f217bc
# seed: 242488664

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i for i in xrange(-(n//2), n//2+1) if not (i == 0 and n%2 == 0)]