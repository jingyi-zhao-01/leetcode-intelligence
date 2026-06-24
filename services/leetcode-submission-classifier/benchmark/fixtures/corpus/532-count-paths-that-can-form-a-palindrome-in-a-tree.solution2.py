# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-paths-that-can-form-a-palindrome-in-a-tree
# source_path: LeetCode-Solutions-master/Python/count-paths-that-can-form-a-palindrome-in-a-tree.py
# solution_class: Solution2
# submission_id: d9ed96d8e319ed84e65f3266676fffe6a01e0f84
# seed: 3750282686

# Time:  O(n)
# Space: O(n)

import collections


# iterative dfs, freq table

class Solution2(object):
    def countPalindromePaths(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        def dfs(u, mask):
            result = 0
            if u:
                mask ^= 1<<(ord(s[u])-ord('a'))
                result += cnt[mask]+sum(cnt[mask^(1<<i)] if mask^(1<<i) in cnt else 0 for i in xrange(26))
                cnt[mask] += 1
            return result+sum(dfs(v, mask) for v in adj[u])

        adj = [[] for _ in xrange(len(parent))]
        for u, p in enumerate(parent):
            if p != -1:
                adj[p].append(u)
        cnt = collections.defaultdict(int)
        cnt[0] = 1
        return dfs(0, 0)