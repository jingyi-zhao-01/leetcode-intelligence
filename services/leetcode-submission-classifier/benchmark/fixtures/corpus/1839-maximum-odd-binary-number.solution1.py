# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-odd-binary-number
# source_path: LeetCode-Solutions-master/Python/maximum-odd-binary-number.py
# solution_class: Solution
# submission_id: d0a8b2f92464fb5c19789667fcb54f0977d22a9b
# seed: 520285960

# Time:  O(n)
# Space: O(1)

# greedy, partition

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = list(s)
        left = 0
        for i in xrange(len(a)):
            if a[i] != '1':
                continue
            a[i], a[left] = a[left], a[i]
            left += 1
        if a[-1] != '1':
            a[-1], a[left-1] = a[left-1], a[-1]
        return "".join(a)