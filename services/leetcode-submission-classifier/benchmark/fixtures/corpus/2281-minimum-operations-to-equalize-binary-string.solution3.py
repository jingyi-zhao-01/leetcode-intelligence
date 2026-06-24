# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-equalize-binary-string
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-equalize-binary-string.py
# solution_class: Solution3
# submission_id: 046b320f087d8a04c97a3a19c25173da3c00c479
# seed: 845304896

# Time:  O(n)
# Space: O(1)

# math

class Solution3(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        zero = s.count('0')
        for i in xrange(len(s)+1):
            if (i*k-zero)&1:
                continue
            if i&1:
                if zero <= i*k <= zero*i+(len(s)-zero)*(i-1):
                    return i
            else:
                if zero <= i*k <= zero*(i-1)+(len(s)-zero)*i:
                    return i
        return -1