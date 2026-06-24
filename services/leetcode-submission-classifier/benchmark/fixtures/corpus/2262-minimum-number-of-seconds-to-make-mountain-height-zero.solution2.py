# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-seconds-to-make-mountain-height-zero
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-seconds-to-make-mountain-height-zero.py
# solution_class: Solution2
# submission_id: 1b0ab4db666d6769a97a167290b23cccadc9bea0
# seed: 2610473362

# Time:  O(nlogr), r = min(workerTimes) * (mountainHeight + 1) * mountainHeight / 2
# Space: O(1)

# binary search, quadratic equation

class Solution2(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        min_heap = [(0+1*t, i, 1) for i, t in enumerate(workerTimes)]
        heapq.heapify(min_heap)
        for _ in xrange(mountainHeight):
            result, i, x = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (result+(x+1)*workerTimes[i], i, x+1))
        return result