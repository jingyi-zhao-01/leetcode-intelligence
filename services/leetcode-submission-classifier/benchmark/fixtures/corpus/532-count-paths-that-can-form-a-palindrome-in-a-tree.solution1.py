# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-paths-that-can-form-a-palindrome-in-a-tree
# source_path: LeetCode-Solutions-master/Python/count-paths-that-can-form-a-palindrome-in-a-tree.py
# solution_class: Solution
# submission_id: 76b41194511507c8cf10e62438240dc87de75912
# seed: 2431750588

# Time:  O(n)
# Space: O(n)

import collections


# iterative dfs, freq table

class Solution(object):
    def countPalindromePaths(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        def iter_dfs():
            result = 0
            cnt = collections.defaultdict(int)
            cnt[0] = 1
            stk = [(0, 0)]
            while stk:
                u, mask = stk.pop()
                if u:
                    mask ^= 1<<(ord(s[u])-ord('a'))
                    result += cnt[mask]+sum(cnt[mask^(1<<i)] if mask^(1<<i) in cnt else 0 for i in xrange(26))
                    cnt[mask] += 1
                for v in reversed(adj[u]):
                    stk.append((v, mask))
            return result

        adj = [[] for _ in xrange(len(parent))]
        for u, p in enumerate(parent):
            if p != -1:
                adj[p].append(u)
        return iter_dfs()