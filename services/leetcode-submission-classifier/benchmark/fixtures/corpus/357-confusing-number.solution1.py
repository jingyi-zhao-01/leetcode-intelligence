# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: confusing-number
# source_path: LeetCode-Solutions-master/Python/confusing-number.py
# solution_class: Solution
# submission_id: 173a00531b72d7654ff4ba13acb5b254c1fda534
# seed: 1601169121

# Time:  O(logn)
# Space: O(logn)

class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        lookup = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        S = str(N)
        result = []
        for i in xrange(len(S)):
            if S[i] not in lookup:
                return False
        for i in xrange((len(S)+1)//2):
            if S[i] != lookup[S[-(i+1)]]:
                return True
        return False