# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-string-with-a-given-numeric-value
# source_path: LeetCode-Solutions-master/Python/smallest-string-with-a-given-numeric-value.py
# solution_class: Solution
# submission_id: 90e186e41a9753893d503385be4ca19d97395f61
# seed: 3146253452

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        MAX_DIFF = ord('z')-ord('a')

        k -= n
        result = ['a']*n
        for i in reversed(xrange(n)):
            tmp = min(k, MAX_DIFF)
            result[i] = chr(ord('a')+tmp)
            k -= tmp
            if k == 0:
                break
        return "".join(result)