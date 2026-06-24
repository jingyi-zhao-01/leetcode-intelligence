# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: meeting-rooms-iii
# source_path: LeetCode-Solutions-master/Python/meeting-rooms-iii.py
# solution_class: Solution2
# submission_id: f1d53515546ccc2f98baf40b7fdc4b964fb699ba
# seed: 3245746117

# Time:  O(mlogm + n + mlogn)
# Space: O(n)

import heapq


# one heap solution

class Solution2(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: 
        """
        meetings.sort()
        unused, used = range(n), []
        result = [0]*n
        for s, e in meetings:
            while used and used[0][0] <= s:
                _, i = heapq.heappop(used)
                heapq.heappush(unused, i)
            if unused:
                i = heapq.heappop(unused)
                heapq.heappush(used, (e, i))
            else:
                e2, i = heapq.heappop(used)
                heapq.heappush(used, (e2+(e-s), i))
            result[i] += 1
        return max(xrange(n), key=lambda x:result[x])