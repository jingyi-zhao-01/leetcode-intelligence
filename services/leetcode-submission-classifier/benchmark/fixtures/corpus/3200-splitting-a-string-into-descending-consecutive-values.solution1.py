# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: splitting-a-string-into-descending-consecutive-values
# source_path: LeetCode-Solutions-master/Python/splitting-a-string-into-descending-consecutive-values.py
# solution_class: Solution
# submission_id: 8e2fb5f05e348221ad0b5d99557e66269b12f07a
# seed: 582399378

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def backtracking(s, i, num, cnt):
            if i == len(s):
                return cnt >= 2
            new_num = 0
            for j in xrange(i, len(s)):
                new_num = new_num*10 + int(s[j])
                if new_num >= num >= 0:
                    break
                if (num == -1 or num-1 == new_num) and backtracking(s, j+1, new_num, cnt+1):
                    return True
            return False
            
        return backtracking(s, 0, -1, 0)