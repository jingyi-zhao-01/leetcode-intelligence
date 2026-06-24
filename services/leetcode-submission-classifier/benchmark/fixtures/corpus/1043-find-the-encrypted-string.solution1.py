# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-encrypted-string
# source_path: LeetCode-Solutions-master/Python/find-the-encrypted-string.py
# solution_class: Solution
# submission_id: 4565cd3593db97cb176a8bc4c1a2f725bebd5d64
# seed: 1715447801

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return "".join(s[(i+k)%len(s)] for i in xrange(len(s)))