# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-peaks
# source_path: LeetCode-Solutions-master/Python/find-the-peaks.py
# solution_class: Solution
# submission_id: f54412805316a9402421aae5972eb7d17877fef8
# seed: 3456268389

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        return [i for i in xrange(1, len(mountain)-1) if mountain[i-1] < mountain[i] > mountain[i+1]]