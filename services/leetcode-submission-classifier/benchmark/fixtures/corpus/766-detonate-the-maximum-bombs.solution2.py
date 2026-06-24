# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: detonate-the-maximum-bombs
# source_path: LeetCode-Solutions-master/Python/detonate-the-maximum-bombs.py
# solution_class: Solution2
# submission_id: de5163b6406af305ba70a156549c300a9707000c
# seed: 281568390

# Time:  O(|V|^2 + |V| * |E|)
# Space: O(|V| + |E|)

# bfs solution

class Solution2(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """        
        adj = [[] for _ in xrange(len(bombs))]
        for i, (xi, yi, ri) in enumerate(bombs):
            for j, (xj, yj, _) in enumerate(bombs):
                if j == i:
                    continue
                if (xi-xj)**2+(yi-yj)**2 <= ri**2:
                    adj[i].append(j)
        result = 0
        for i in xrange(len(bombs)):
            stk = [i]
            lookup = {i}
            while stk:
                u = stk.pop()
                for v in adj[u]:
                    if v in lookup:
                        continue
                    lookup.add(v)
                    stk.append(v)
            result = max(result, len(lookup))
            if result == len(bombs):
                break
        return result