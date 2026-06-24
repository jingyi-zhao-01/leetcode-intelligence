# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kill-process
# source_path: LeetCode-Solutions-master/Python/kill-process.py
# solution_class: Solution2
# submission_id: d9596c5c4942fc880e15c8b2b6c24f3029f0da4e
# seed: 195277584

# Time:  O(n)
# Space: O(n)

import collections


# DFS solution.

class Solution2(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        def killAll(pid, children, killed):
            killed.append(pid)
            for child in children[pid]:
                killAll(child, children, killed)

        result = []
        children = collections.defaultdict(set)
        for i in xrange(len(pid)):
            children[ppid[i]].add(pid[i])
        q = collections.deque()
        q.append(kill)
        while q:
            p = q.popleft()
            result.append(p)
            for child in children[p]:
                q.append(child)
        return result