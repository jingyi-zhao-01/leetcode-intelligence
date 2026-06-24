# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-string-contains-all-binary-codes-of-size-k
# source_path: LeetCode-Solutions-master/Python/check-if-a-string-contains-all-binary-codes-of-size-k.py
# solution_class: Solution
# submission_id: 6a92ea512888dbb77c554922f79b7c7d76b155ed
# seed: 3523011000

# Time:  O(n * k)
# Space: O(k * 2^k)

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return 2**k <= len(s) and len({s[i:i+k] for i in xrange(len(s)-k+1)}) == 2**k