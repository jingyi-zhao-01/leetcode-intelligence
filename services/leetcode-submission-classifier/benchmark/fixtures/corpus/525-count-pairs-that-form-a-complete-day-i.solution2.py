# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-that-form-a-complete-day-i
# source_path: LeetCode-Solutions-master/Python/count-pairs-that-form-a-complete-day-i.py
# solution_class: Solution2
# submission_id: cc72f1786ea984cf289f4fdf4f113eb623be8339
# seed: 2545552090

# Time:  O(n + 24)
# Space: O(24)

# freq table

class Solution2(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        return sum((hours[i]+hours[j])%24 == 0 for i in xrange(len(hours)-1) for j in xrange(i+1, len(hours)))