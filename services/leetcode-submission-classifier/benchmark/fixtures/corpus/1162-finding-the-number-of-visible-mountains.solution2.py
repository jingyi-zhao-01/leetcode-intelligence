# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: finding-the-number-of-visible-mountains
# source_path: LeetCode-Solutions-master/Python/finding-the-number-of-visible-mountains.py
# solution_class: Solution2
# submission_id: 72f81b0978695ec8d2f5171802d9e07b0026e001
# seed: 278072907

# Time:  O(nlogn)
# Space: O(1)

# math, sort

class Solution2(object):
    def visibleMountains(self, peaks):
        """
        :type peaks: List[List[int]]
        :rtype: int
        """
        def is_covered(a, b):
            x1, y1 = a
            x2, y2 = b
            return x2-y2 <= x1-y1 and x1+y1 <= x2+y2

        peaks.sort()
        stk = []
        for i in xrange(len(peaks)):
            while stk and is_covered(peaks[stk[-1]], peaks[i]):
                stk.pop()
            if (i-1 == -1 or peaks[i-1] != peaks[i]) and (not stk or not is_covered(peaks[i], peaks[stk[-1]])):  # not duplicted and not covered
                stk.append(i)
        return len(stk)