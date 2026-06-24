# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-from-optimal-activation-order
# source_path: LeetCode-Solutions-master/Python/maximum-total-from-optimal-activation-order.py
# solution_class: Solution
# submission_id: ea3f762a96c35099b8af4e30ddb03aa37d96edf6
# seed: 3457674938

# Time:  O(nlogn)
# Space: O(n)

# sort, greedy

class Solution(object):
    def maxTotal(self, value, limit):
        """
        :type value: List[int]
        :type limit: List[int]
        :rtype: int
        """
        idxs = range(len(value))
        idxs.sort(key=lambda x: (limit[x], -value[x]))
        result = cnt = prev = 0
        for i in idxs:
            l, v = limit[i], value[i]
            if l != prev:
                cnt = 0
                prev = l
            if cnt < l:
                result += v
                cnt += 1
        return result