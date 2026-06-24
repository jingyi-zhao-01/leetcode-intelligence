# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-subtree-sizes-after-changes
# source_path: LeetCode-Solutions-master/Python/find-subtree-sizes-after-changes.py
# solution_class: Solution2
# submission_id: aa8118b76d75b9d7d8e4858556ee6b1cac251991
# seed: 4044697386

# Time:  O(n)
# Space: O(n)

# iterative dfs, hash table

class Solution2(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        def dfs(u):
            lookup[ord(s[u])-ord('a')].append(u)
            for v in adj[u]:
                dfs(v)
                result[lookup[ord(s[v])-ord('a')][-1] if lookup[ord(s[v])-ord('a')] else u] += result[v]
            lookup[ord(s[u])-ord('a')].pop()
        
        adj = [[] for _ in xrange(len(parent))]
        for v, u in enumerate(parent):
            if u != -1:
                adj[u].append(v)
        lookup = [[] for _ in xrange(26)]
        result = [1]*len(parent)
        dfs(0)
        return result