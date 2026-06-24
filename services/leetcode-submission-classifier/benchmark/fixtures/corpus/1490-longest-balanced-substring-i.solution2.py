# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-balanced-substring-i
# source_path: LeetCode-Solutions-master/Python/longest-balanced-substring-i.py
# solution_class: Solution2
# submission_id: 78971a6981266a11a71c82658ab879b7bef968a1
# seed: 2374210043

# Time:  O(n * (a + n))), a = len(set(s))
# Space: O(a)

import collections


# freq table

class Solution2(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(s)):
            cnt = [0]*26
            mx = unique = 0
            for j in xrange(i, len(s)):
                if cnt[ord(s[j])-ord('a')] == 0:
                    unique += 1
                cnt[ord(s[j])-ord('a')] += 1
                mx = max(mx, cnt[ord(s[j])-ord('a')])
                if (j-i+1)%unique == 0 and (j-i+1)//unique == mx:
                    result = max(result, j-i+1)
        return result