# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-distance-in-arrays
# source_path: LeetCode-Solutions-master/Python/maximum-distance-in-arrays.py
# solution_class: Solution
# submission_id: 1302f2805f894be67bc57e125a42f89194c7a617
# seed: 2131932033

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        result, min_val, max_val = 0,  arrays[0][0], arrays[0][-1]
        for i in xrange(1, len(arrays)):
            result = max(result, \
                         max(max_val - arrays[i][0], \
                             arrays[i][-1] - min_val))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return result