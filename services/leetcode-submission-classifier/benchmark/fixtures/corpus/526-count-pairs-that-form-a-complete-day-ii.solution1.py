# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-that-form-a-complete-day-ii
# source_path: LeetCode-Solutions-master/Python/count-pairs-that-form-a-complete-day-ii.py
# solution_class: Solution
# submission_id: 9d00e7e26615bc81215ee368f5ccfc7bde13cb20
# seed: 1657064971

# Time:  O(n + 24)
# Space: O(24)

# freq table

class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        result = 0
        cnt = [0]*24
        for x in hours:
            result += cnt[-x%24]
            cnt[x%24] += 1
        return result