# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-good-days-to-rob-the-bank
# source_path: LeetCode-Solutions-master/Python/find-good-days-to-rob-the-bank.py
# solution_class: Solution
# submission_id: 7e5a4e56776971b7ba39cc99aa14edfe429ab543
# seed: 1353045603

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        right = [0]
        for i in reversed(xrange(1, len(security))):
            right.append(right[-1]+1 if security[i] >= security[i-1] else 0)
        right.reverse()
        result = []
        left = 0
        for i in xrange(len(security)):
            if left >= time and right[i] >= time:
                result.append(i)
            if i+1 < len(security):
                left = left+1 if security[i] >= security[i+1] else 0
        return result