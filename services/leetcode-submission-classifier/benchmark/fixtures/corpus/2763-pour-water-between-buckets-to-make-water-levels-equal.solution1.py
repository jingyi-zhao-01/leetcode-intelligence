# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pour-water-between-buckets-to-make-water-levels-equal
# source_path: LeetCode-Solutions-master/Python/pour-water-between-buckets-to-make-water-levels-equal.py
# solution_class: Solution
# submission_id: 1d1d110a499cd90fdc40bfb07b18acddf54dfefa
# seed: 3307798117

# Time:  O(nlogr)
# Space: O(1)

# binary search

class Solution(object):
    def equalizeWater(self, buckets, loss):
        """
        :type buckets: List[int]
        :type loss: int
        :rtype: float
        """
        def check(buckets, rate, x):
            return sum(b-x for b in buckets if b-x > 0)*rate >= sum(x-b for b in buckets if x-b > 0)

        EPS = 1e-5
        rate = (100-loss)/100.0
        left, right = float(min(buckets)), float(sum(buckets))/len(buckets)
        while right-left > EPS:
            mid = left + (right-left)/2
            if not check(buckets, rate, mid):
                right = mid
            else:
                left = mid
        return left