# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-array-modulo-alternating-ii
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-array-modulo-alternating-ii.py
# solution_class: Solution
# submission_id: 02c744029d16772cedc4ba4a2f9119d9508c2f93
# seed: 986732935

# Time:  O(n + k)
# Space: O(k)

# freq table, sliding window

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def topk(a, k):  # Time: O(k * n)
            result = [(float("inf"), float("inf"))]*k
            for idx, x in enumerate(a):
                tmp = (x, idx)
                for i in xrange(len(result)):
                    if tmp < result[i]:
                        result[i], tmp = tmp, result[i]
            return result

        def distance(cnt):
            total = sum(cnt)
            c = sum(cnt[i] for i in xrange(1, k//2+1))
            dist = [0]*k
            dist[0] = sum(x*min(i, k-i) for i, x in enumerate(cnt))
            for i in xrange(1, len(dist)):
                dist[i] = dist[i-1]-c+(total-c)-(cnt[((i+k//2))%k] if k%2 else 0)
                c += cnt[((i+k//2))%k]-cnt[i]
            return dist

        cnt = [[0]*k for _ in xrange(2)]
        for i, x in enumerate(nums):
            cnt[i%2][x%k] += 1
        dist = [distance(cnt[i]) for i in xrange(2)]
        top2 = [topk(dist[i], 2) for i in xrange(2)]
        return min(top2[0][0][0]+top2[1][1][0], top2[0][1][0]+top2[1][0][0]) if top2[0][0][1] == top2[1][0][1] else top2[0][0][0]+top2[1][0
][0]