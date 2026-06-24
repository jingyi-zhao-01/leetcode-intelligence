# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-activate-string
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-activate-string.py
# solution_class: Solution
# submission_id: d186953c5449a85c79433b614896ac120bbdb4c8
# seed: 2701882296

# Time:  O(n)
# Space: O(n)

# backward simulation, doubly linked list

class Solution(object):
    def minTime(self, s, order, k):
        """
        :type s: str
        :type order: List[int]
        :type k: int
        :rtype: int
        """
        left = range(-1, len(s)-1)
        right = range(1, len(s)+1)
        cnt = (len(s)+1)*len(s)//2
        if cnt < k:
            return -1
        for t in reversed(xrange(len(order))):
            i = order[t]
            l = left[i]
            r = right[i]
            cnt -= (i-l)*(r-i)
            if cnt < k:
                break
            if l >= 0:
                right[l] = r
            if r < len(left):
                left[r] = l
        return t