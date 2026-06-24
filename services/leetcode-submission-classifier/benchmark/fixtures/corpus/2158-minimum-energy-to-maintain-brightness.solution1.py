# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-energy-to-maintain-brightness
# source_path: LeetCode-Solutions-master/Python/minimum-energy-to-maintain-brightness.py
# solution_class: Solution
# submission_id: 567f7a91e9834508ec39c357e4d74708b3223bf1
# seed: 1095026312

# Time:  O(nlogn)
# Space: O(1)

# sort, line sweep

class Solution(object):
    def minEnergy(self, n, brightness, intervals):
        """
        :type n: int
        :type brightness: int
        :type intervals: List[List[int]]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        intervals.sort(key=lambda x: x[0])
        result = 0
        left, right = 0, -1
        for l, r in intervals:
            if l <= right+1:
                right = max(right, r)
                continue
            result += right-left+1
            left, right = l, r
        result += right-left+1
        result *= ceil_divide(brightness, 3)
        return result