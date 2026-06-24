# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-all-the-integers-in-a-range-are-covered
# source_path: LeetCode-Solutions-master/Python/check-if-all-the-integers-in-a-range-are-covered.py
# solution_class: Solution3
# submission_id: c87f19f6e74106acdb3c81bfc5ad5567d30bc081
# seed: 3827380402

# Time:  O(n + r)
# Space: O(r)

# if r is small, this is better

class Solution3(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        return all(any(l <= i <= r for l, r in ranges) for i in xrange(left, right+1))