# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-people-with-secret
# source_path: LeetCode-Solutions-master/Python/find-all-people-with-secret.py
# solution_class: Solution3
# submission_id: 29e824184cbfaef04ba06b6c28e1e2bd9032508b
# seed: 2444916934

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution3(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        meetings.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        uf.union_set(0, firstPerson)
        group = set()
        for i, (x, y, _) in enumerate(meetings):
            group.add(x)
            group.add(y)
            uf.union_set(x, y)
            if i+1 != len(meetings) and meetings[i+1][2] == meetings[i][2]:
                continue
            while group:
                x = group.pop()
                if uf.find_set(x) != uf.find_set(0):
                    uf.reset(x)
        return [i for i in xrange(n) if uf.find_set(i) == uf.find_set(0)]