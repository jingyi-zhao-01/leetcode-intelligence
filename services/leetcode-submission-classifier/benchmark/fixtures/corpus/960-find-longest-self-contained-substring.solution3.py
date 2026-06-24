# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-longest-self-contained-substring
# source_path: LeetCode-Solutions-master/Python/find-longest-self-contained-substring.py
# solution_class: Solution3
# submission_id: c10c78db818c65d31e309ca93c7776e301ef0a10
# seed: 3054859897

# Time:  O(n + 26^3 * logn)
# Space: O(n)

import bisect


# hash table, binary search

class Solution3(object):
    def maxSubstringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        def update(x, d, distinct, valid):
            x = ord(x)-ord('a')
            if cnt2[x] == cnt[x]:
                valid -= 1
            if cnt2[x] == 0:
                distinct += 1
            cnt2[x] += d
            if cnt2[x] == 0:
                distinct -= 1
            if cnt2[x] == cnt[x]:
                valid += 1
            return distinct, valid
                
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        result = -1
        for l in xrange(1, sum(x != 0 for x in cnt)):
            cnt2 = [0]*26
            left = distinct = valid = 0
            for right in xrange(len(s)):
                distinct, valid = update(s[right], +1, distinct, valid)
                while distinct == l+1:
                    distinct, valid = update(s[left], -1, distinct, valid)
                    left += 1
                if valid == l:
                    result = max(result, right-left+1)
        return result