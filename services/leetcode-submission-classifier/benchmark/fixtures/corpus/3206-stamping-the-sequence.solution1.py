# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stamping-the-sequence
# source_path: LeetCode-Solutions-master/Python/stamping-the-sequence.py
# solution_class: Solution
# submission_id: 1ad8ae8dacf30f9ca4002a03f9fd24328eb54c52
# seed: 2216132925

# Time:  O((n - m) * m)
# Space: O((n - m) * m)

import collections

class Solution(object):
    def movesToStamp(self, stamp, target):
        M, N = len(stamp), len(target)

        q = collections.deque()
        lookup = [False]*N
        result = []
        A = []
        for i in xrange(N-M+1):
            made, todo = set(), set()
            for j, c in enumerate(stamp):
                if c == target[i+j]:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))
            if todo:
                continue
            result.append(i)
            for m in made:
                if lookup[m]:
                    continue
                q.append(m)
                lookup[m] = True

        while q:
            i = q.popleft()
            for j in xrange(max(0, i-M+1), min(N-M, i)+1):
                made, todo = A[j]
                if i not in todo:
                    continue
                todo.discard(i)
                if todo:
                    continue
                result.append(j)
                for m in made:
                    if lookup[m]:
                        continue
                    q.append(m)
                    lookup[m] = True
        return result[::-1] if all(lookup) else []