# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-zero-request-servers
# source_path: LeetCode-Solutions-master/Python/count-zero-request-servers.py
# solution_class: Solution
# submission_id: 52a60d5b2bc547d3da4e622e06d93c3916b8818d
# seed: 200712720

# Time:  O(nlogn + mlogm)
# Space: O(n + m)

# sort, two pointers

class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs.sort(key=lambda x:x[1])
        result = [0]*len(queries)
        cnt = [0]*n
        curr = left = right = 0
        for t, i in sorted((t, i) for i, t in enumerate(queries)):
            while right < len(logs) and logs[right][1] <= t:
                if cnt[logs[right][0]-1] == 0:
                    curr += 1
                cnt[logs[right][0]-1] += 1
                right += 1
            while left < right and logs[left][1] < t-x:
                cnt[logs[left][0]-1] -= 1
                if cnt[logs[left][0]-1] == 0:
                    curr -= 1
                left += 1
            result[i] = n-curr
        return result