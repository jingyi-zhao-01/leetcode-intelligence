# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-balanced-substring-after-one-swap
# source_path: LeetCode-Solutions-master/Python/longest-balanced-substring-after-one-swap.py
# solution_class: Solution
# submission_id: f09fe9419fbe8d92125cc7eb6cd1cb344a7ebfbf
# seed: 279626118

# Time:  O(n)
# Space: O(n)

import collections


# hash table

class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt0 = s.count('0')
        cnt1 = len(s)-cnt0
        if cnt0 < cnt1:
            cnt0, cnt1 = cnt1, cnt0
            s = "".join('0' if x == '1' else '1' for x in s)
        result = bal = 0
        lookup = collections.defaultdict(list)
        lookup[0].append(-1)
        for i, x in enumerate(s):
            bal += +1 if x == '1' else -1
            if len(lookup[bal]) != 2:
                lookup[bal].append(i)
            result = max(result, i-lookup[bal][0])
            for j in lookup[bal+2]:
                if (i-j-2)//2 != cnt1:
                    result = max(result, i-j)
                    break
        return result