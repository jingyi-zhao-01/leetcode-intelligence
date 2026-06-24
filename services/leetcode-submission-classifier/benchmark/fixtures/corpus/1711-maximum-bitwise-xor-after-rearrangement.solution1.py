# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-bitwise-xor-after-rearrangement
# source_path: LeetCode-Solutions-master/Python/maximum-bitwise-xor-after-rearrangement.py
# solution_class: Solution
# submission_id: 648875cb260bc20c2cd76ba252f5e28793a76ded
# seed: 3997511151

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maximumXor(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt = [t.count('0'), t.count('1')]
        result = []
        for i in xrange(len(s)):
            x = ord(s[i])-ord('0')
            if cnt[x^1]:
                cnt[x^1] -= 1
                result.append('1')
            else:
                cnt[x] -= 1
                result.append('0')
        return "".join(result)