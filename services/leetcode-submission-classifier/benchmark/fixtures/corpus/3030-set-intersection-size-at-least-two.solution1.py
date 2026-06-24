# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: set-intersection-size-at-least-two
# source_path: LeetCode-Solutions-master/Python/set-intersection-size-at-least-two.py
# solution_class: Solution
# submission_id: ec03e45a19155eb1e94ba6c7c189f72f27945bf9
# seed: 226299553

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda s_e: (s_e[0], -s_e[1]))
        cnts = [2] * len(intervals)
        result = 0
        while intervals:
            (start, _), cnt = intervals.pop(), cnts.pop()
            for s in xrange(start, start+cnt):
                for i in xrange(len(intervals)):
                    if cnts[i] and s <= intervals[i][1]:
                        cnts[i] -= 1
            result += cnt
        return result