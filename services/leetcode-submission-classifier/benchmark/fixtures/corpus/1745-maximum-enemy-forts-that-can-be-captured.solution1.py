# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-enemy-forts-that-can-be-captured
# source_path: LeetCode-Solutions-master/Python/maximum-enemy-forts-that-can-be-captured.py
# solution_class: Solution
# submission_id: 23117b8c6c6ea2c46aa2572e5963254a9661a292
# seed: 2173534980

# Time:  O(n)
# Space: O(1)

# array, two pointers

class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        result = left = 0
        for right in xrange(len(forts)):
            if not forts[right]:
                continue
            if forts[right] == -forts[left]:
                result = max(result, right-left-1)
            left = right
        return result