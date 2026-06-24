# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-string-after-applying-operations
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-string-after-applying-operations.py
# solution_class: Solution2
# submission_id: 34b80c7d222b983141e4b3498a19587701bd6aba
# seed: 2347922284

# Time:  O(100 * n^2) = O(n^2)
# Space: O(1)

class Solution2(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        q, lookup, result = collections.deque([s]), {s}, s
        while q:
            curr = q.popleft()
            if curr < result:
                result = curr
            add_a = list(curr)    
            for i, c in enumerate(add_a):
                if i%2:
                    add_a[i] = str((int(c)+a) % 10)
            add_a = "".join(add_a)        
            if add_a not in lookup:
                lookup.add(add_a)
                q.append(add_a)
            rotate_b = curr[b:] + curr[:b]
            if rotate_b not in lookup:
                lookup.add(rotate_b)
                q.append(rotate_b)
        return result