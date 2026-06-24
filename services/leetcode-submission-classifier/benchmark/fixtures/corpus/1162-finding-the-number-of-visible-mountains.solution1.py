# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: finding-the-number-of-visible-mountains
# source_path: LeetCode-Solutions-master/Python/finding-the-number-of-visible-mountains.py
# solution_class: Solution
# submission_id: 3116696160dd77213e13c9a76f74d06b3c085418
# seed: 2404412069

# Time:  O(nlogn)
# Space: O(1)

# math, sort

class Solution(object):
    def visibleMountains(self, peaks):
        """
        :type peaks: List[List[int]]
        :rtype: int
        """
        peaks.sort(key=lambda x: (x[0]-x[1], -(x[0]+x[1])))  # rotate points by 45 degrees and we only care the largest new y in the same new x
        result = mx = 0
        for i in xrange(len(peaks)):
            if peaks[i][0]+peaks[i][1] <= mx:
                continue
            mx = peaks[i][0]+peaks[i][1]
            if i+1 == len(peaks) or peaks[i+1] != peaks[i]:
                result += 1
        return result