# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-zero-request-servers
# source_path: LeetCode-Solutions-master/Python/count-zero-request-servers.py
# solution_class: Solution2
# submission_id: dca00288388c9db91d8f1774c4dfdc2bd22f9d32
# seed: 1594122134

# Time:  O(nlogn + mlogm)
# Space: O(n + m)

# sort, two pointers

class Solution2(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        events = []
        for sid, t in logs:
            events.append((t, +1, sid-1))
            events.append((t+x+1, -1, sid-1))
        events.append((float("inf"), 0, 0))
        events.sort()

        events2 = []
        for i, t in enumerate(queries):
            events2.append((t, i))
        events2.sort(reverse=True)

        result = [0]*len(queries)
        cnt = [0]*n
        curr = 0
        for t, c, i in events:
            while events2 and events2[-1][0] < t:                
                result[events2.pop()[1]] += n-curr
            if cnt[i] == 0:
                curr += 1
            cnt[i] += c
            if cnt[i] == 0:
                curr -= 1
        return result