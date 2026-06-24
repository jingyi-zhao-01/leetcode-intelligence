# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-subtree-sizes-after-changes
# source_path: LeetCode-Solutions-master/Python/find-subtree-sizes-after-changes.py
# solution_class: Solution
# submission_id: 29b5a5edf044a8a2cbbd1a872ac9884562fb88bf
# seed: 3770060814

# Time:  O(n)
# Space: O(n)

# iterative dfs, hash table

class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        def iter_dfs():
            lookup = [[] for _ in xrange(26)]
            result = [1]*len(parent)
            stk = [(1, 0)]
            while stk:
                step, u = stk.pop()
                if step == 1:
                    lookup[ord(s[u])-ord('a')].append(u)
                    stk.append((2, u))
                    for v in reversed(adj[u]):
                        stk.append((1, v))
                elif step == 2:
                    for v in adj[u]:
                        result[lookup[ord(s[v])-ord('a')][-1] if lookup[ord(s[v])-ord('a')] else u] += result[v]
                    lookup[ord(s[u])-ord('a')].pop()
            return result
        
        adj = [[] for _ in xrange(len(parent))]
        for v, u in enumerate(parent):
            if u != -1:
                adj[u].append(v)
        return iter_dfs()