# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-element-after-decreasing-and-rearranging
# source_path: LeetCode-Solutions-master/Python/maximum-element-after-decreasing-and-rearranging.py
# solution_class: Solution
# submission_id: 0e49342fd8b914bf1939aee6daada19d1ba05457
# seed: 2385259794

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        result = 1
        for i in xrange(1, len(arr)):
            result = min(result+1, arr[i])
        return result