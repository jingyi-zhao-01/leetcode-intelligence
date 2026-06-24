# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-people-with-secret
# source_path: LeetCode-Solutions-master/Python/find-all-people-with-secret.py
# solution_class: Solution2
# submission_id: bf7c0287040a89163209ccb9e15ce78977cee453
# seed: 1285487715

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution2(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        meetings.sort(key=lambda x: x[2])
        result = {0, firstPerson}
        adj = collections.defaultdict(list)
        for i, (x, y, _) in enumerate(meetings):
            adj[x].append(y)
            adj[y].append(x)
            if i+1 != len(meetings) and meetings[i+1][2] == meetings[i][2]:
                continue
            stk = [i for i in adj.iterkeys() if i in result]
            while stk:
                u = stk.pop()
                for v in adj[u]:
                    if v in result:
                        continue
                    result.add(v)
                    stk.append(v)
            adj = collections.defaultdict(list)
        return list(result)