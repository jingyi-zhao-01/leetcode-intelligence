# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-waviness-of-numbers-in-range-i
# source_path: LeetCode-Solutions-master/Python/total-waviness-of-numbers-in-range-i.py
# solution_class: Solution
# submission_id: 1dc1488c2626d8974766f119d185ca87bef73559
# seed: 1227464123

# Time:  O(nlogn)
# Space: O(logn)

# brute force

class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        result = 0
        for i in xrange(num1, num2+1):
            s = str(i)
            for i in xrange(1, len(s)-1):
                if s[i-1] < s[i] > s[i+1] or s[i-1] > s[i] < s[i+1]:
                    result += 1
        return result