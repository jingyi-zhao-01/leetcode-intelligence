# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-string-that-contains-three-strings
# source_path: LeetCode-Solutions-master/Python/shortest-string-that-contains-three-strings.py
# solution_class: Solution2
# submission_id: 9caf2e7d31e7a0c15333e1274498a369686f817c
# seed: 1021775471

# Time:  O(l)
# Space: O(l)

# brute force, longest prefix suffix, kmp algorithm

class Solution2(object):
    def minimumString(self, a, b, c):
        """
        :type a: str
        :type b: str
        :type c: str
        :rtype: str
        """
        def merge(a, b):
            if a in b:
                return b
            l = next((l for l in reversed(xrange(1, min(len(a), len(b)))) if a[-l:] == b[:l]), 0)
            return a+b[l:]

        result = [merge(a, merge(b, c)), merge(a, merge(c, b)),
                  merge(b, merge(a, c)), merge(b, merge(c, a)),
                  merge(c, merge(a, b)), merge(c, merge(b, a))]
        return min(result, key=lambda x: (len(x), x))