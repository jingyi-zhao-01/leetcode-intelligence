# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-genetic-mutation
# source_path: LeetCode-Solutions-master/Python/minimum-genetic-mutation.py
# solution_class: Solution
# submission_id: a7a4be700465a8e9e80129e6b2fb0bfbd0f1c142
# seed: 1120872964

# Time:  O(n * b), n is the length of gene string, b is size of bank
# Space: O(b)

from collections import deque

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        lookup = {}
        for b in bank:
            lookup[b] = False

        q = deque([(start, 0)])
        while q:
            cur, level = q.popleft()
            if cur == end:
                return level

            for i in xrange(len(cur)):
                for c in ['A', 'T', 'C', 'G']:
                    if cur[i] == c:
                        continue

                    next_str = cur[:i] + c + cur[i+1:]
                    if next_str in lookup and lookup[next_str] == False:
                        q.append((next_str, level+1))
                        lookup[next_str] = True

        return -1