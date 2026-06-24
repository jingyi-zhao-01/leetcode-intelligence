# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-beauty-of-all-substrings
# source_path: LeetCode-Solutions-master/Python/sum-of-beauty-of-all-substrings.py
# solution_class: Solution
# submission_id: da0026eacf1631a908eff5592b4ca59f420bc5a4
# seed: 2197908876

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0 
        for i in xrange(len(s)):
            lookup = [0]*26
            for j in xrange(i, len(s)):
                lookup[ord(s[j])-ord('a')] += 1
                result += max(lookup) - min(x for x in lookup if x)
        return result