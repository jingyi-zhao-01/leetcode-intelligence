# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-dfs-strings-are-palindromes
# source_path: LeetCode-Solutions-master/Python/check-if-dfs-strings-are-palindromes.py
# solution_class: Solution2
# submission_id: fe02d37a452054192a35115e5d48fdc6d1e3899b
# seed: 1376030115

# Time:  O(n)
# Space: O(n)

# iterative dfs, manacher's algorithm

class Solution2(object):
    def findAnswer(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[bool]
        """
        def manacher(s):
            s = '^#' + '#'.join(s) + '#$'
            P = [0]*len(s)
            C, R = 0, 0
            for i in xrange(1, len(s)-1):
                i_mirror = 2*C-i
                if R > i:
                    P[i] = min(R-i, P[i_mirror])
                while s[i+1+P[i]] == s[i-1-P[i]]:
                    P[i] += 1
                if i+P[i] > R:
                    C, R = i, i+P[i]
            return P
    
        def dfs(u):
            left = cnt[0]
            for v in adj[u]:
                dfs(v)
            curr.append(s[u])
            lookup[u] = (left, cnt[0])
            cnt[0] += 1

        adj = [[] for _ in xrange(len(parent))]
        for v in xrange(1, len(parent)):
            adj[parent[v]].append(v)
        cnt = [0]
        curr = []
        lookup = [None]*len(adj)
        dfs(0)
        P = manacher(curr)
        return [P[(2*(left+1)+2*(right+1))//2] >= right-left+1 for left, right in lookup]