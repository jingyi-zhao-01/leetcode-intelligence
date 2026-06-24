# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-binary-substrings
# source_path: LeetCode-Solutions-master/Python/count-binary-substrings.py
# solution_class: Solution
# submission_id: 915cf84ac41e644f23c46e2fbbeede67a65cf02f
# seed: 3331642743

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, prev, curr = 0, 0, 1
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                result += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        result += min(prev, curr)
        return result