# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-all-the-integers-in-a-range-are-covered
# source_path: LeetCode-Solutions-master/Python/check-if-all-the-integers-in-a-range-are-covered.py
# solution_class: Solution
# submission_id: 64eafcda6d5f8ec73495dddb9d4b10779f9a711f
# seed: 921681220

# Time:  O(n + r)
# Space: O(r)

# if r is small, this is better

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        RANGE_SIZE = 50

        interval = [0]*(RANGE_SIZE+1)
        for l, r in ranges:
            interval[l-1] += 1
            interval[(r-1)+1] -= 1
        cnt = 0
        for i in xrange((right-1)+1):
            cnt += interval[i]
            if i >= left-1 and not cnt:
                return False
        return True