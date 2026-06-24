# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-3-same-digit-number-in-string
# source_path: LeetCode-Solutions-master/Python/largest-3-same-digit-number-in-string.py
# solution_class: Solution
# submission_id: b74e216727c9e6385761e26457b1a01c8624006f
# seed: 564879589

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = ''
        cnt = 0
        for i, x in enumerate(num):
            cnt += 1
            if i+1 < len(num) and num[i] == num[i+1]:
                continue
            if cnt >= 3:
                result = max(result, num[i])
            cnt = 0
        return result*3