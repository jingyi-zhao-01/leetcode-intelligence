# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-confusion-of-an-exam
# source_path: LeetCode-Solutions-master/Python/maximize-the-confusion-of-an-exam.py
# solution_class: Solution
# submission_id: 2eec4ce6b2b39665a8823185b99c44a80a20003f
# seed: 289601519

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        result = max_count = 0
        count = collections.Counter()
        for i in xrange(len(answerKey)):
            count[answerKey[i]] += 1
            max_count = max(max_count, count[answerKey[i]])
            if result-max_count >= k:
                count[answerKey[i-result]] -= 1
            else:
                result += 1
        return result