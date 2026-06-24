# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: substring-xor-queries
# source_path: LeetCode-Solutions-master/Python/substring-xor-queries.py
# solution_class: Solution
# submission_id: a289cc558ec37397ef6a786f0ef8da47e601858e
# seed: 932817211

# Time:  O(n * logr + q), r = max(a^b for a, b in queries)
# Space: O(min(n * logr, r))

# hash table

class Solution(object):
    def substringXorQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        mx = max(a^b for a, b in queries)
        lookup = {}
        for i in xrange(len(s)):
            curr = 0
            for j in xrange(i, len(s)):
                curr = (curr<<1)+int(s[j])
                if curr > mx:
                    break
                if curr not in lookup:
                    lookup[curr] = [i, j]
                if s[i] == '0':
                    break
        return [lookup[a^b] if a^b in lookup else [-1, -1] for a, b in queries]