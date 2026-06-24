# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-powerful-integers
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-powerful-integers.py
# solution_class: Solution2
# submission_id: 6b2c2ad226828a4a44189aa3b142e108435fa215
# seed: 294746771

# Time:  O(logf)
# Space: O(1)

# math, combinatorics

class Solution2(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        def count(x):
            result = 0
            str_x = str(x)
            l = len(str_x)-len(s)
            cnt = (limit+1)**l
            for i in xrange(l):
                cnt //= limit+1
                result += (min(int(str_x[i])-1, limit)-0+1)*cnt
                if int(str_x[i]) > limit:
                    break
            else:
                if int(str_x[-len(s):]) >= int(s):
                    result += 1
            return result

        return count(finish)-count(start-1)