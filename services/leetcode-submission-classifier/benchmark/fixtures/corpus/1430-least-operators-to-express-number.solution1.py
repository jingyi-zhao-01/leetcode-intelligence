# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: least-operators-to-express-number
# source_path: LeetCode-Solutions-master/Python/least-operators-to-express-number.py
# solution_class: Solution
# submission_id: 0336d7b71d6ec414800fc8ce518c854f5db70006
# seed: 1544588120

# Time:  O(logn/logx) = O(1)
# Space: O(logn) = O(1)

class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        pos, neg, k = 0, 0, 0
        while target:
            target, r = divmod(target, x)
            if k:
                pos, neg = min(r*k + pos, (r+1)*k + neg), \
                           min((x-r)*k + pos, (x-r-1)*k + neg)
            else:
                pos, neg = r*2, (x-r)*2
            k += 1
        return min(pos, k+neg) - 1