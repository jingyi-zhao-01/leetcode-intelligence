# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: statistics-from-a-large-sample
# source_path: LeetCode-Solutions-master/Python/statistics-from-a-large-sample.py
# solution_class: Solution
# submission_id: cecbedecca521ff0a4255e8dfb79be8f59a7dc85
# seed: 3882646299

# Time:  O(n)
# Space: O(1)

import bisect

class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        n = sum(count)
        mi = next(i for i in xrange(len(count)) if count[i]) * 1.0
        ma = next(i for i in reversed(xrange(len(count))) if count[i]) * 1.0
        mean = sum(i * v for i, v in enumerate(count)) * 1.0 / n
        mode = count.index(max(count)) * 1.0
        for i in xrange(1, len(count)):
            count[i] += count[i-1]
        median1 = bisect.bisect_left(count, (n+1) // 2)
        median2 = bisect.bisect_left(count, (n+2) // 2)
        median = (median1+median2) / 2.0
        return [mi, ma, mean, median, mode]