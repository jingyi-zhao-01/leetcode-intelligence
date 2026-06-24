# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-all-the-integers-in-a-range-are-covered
# source_path: LeetCode-Solutions-master/Python/check-if-all-the-integers-in-a-range-are-covered.py
# solution_class: Solution2
# submission_id: f8ec2eee97c3e6e6b10627b4d20fded1fc6acde5
# seed: 77358656

# Time:  O(n + r)
# Space: O(r)

# if r is small, this is better

class Solution2(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort()
        for l, r in ranges:
            if l <= left <= r:
                left = r+1
        return left > right