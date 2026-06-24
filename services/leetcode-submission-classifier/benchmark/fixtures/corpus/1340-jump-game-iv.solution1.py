# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-iv
# source_path: LeetCode-Solutions-master/Python/jump-game-iv.py
# solution_class: Solution
# submission_id: 7be083ac43c6bc300f70510212c897a6046048d1
# seed: 3308720342

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        groups = collections.defaultdict(list)
        for i, x in enumerate(arr):
            groups[x].append(i)
        q = collections.deque([(0, 0)])
        lookup = set([0])
        while q:
            pos, step = q.popleft()
            if pos == len(arr)-1:
                break
            neighbors = set(groups[arr[pos]] + [pos-1, pos+1])
            groups[arr[pos]] = []
            for p in neighbors:
                if p in lookup or not 0 <= p < len(arr):
                    continue
                lookup.add(p)
                q.append((p, step+1)) 
        return step