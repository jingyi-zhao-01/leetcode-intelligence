# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: query-kth-smallest-trimmed-number
# source_path: LeetCode-Solutions-master/Python/query-kth-smallest-trimmed-number.py
# solution_class: Solution
# submission_id: 909212d90616b05fef7136482e7cf12484647565
# seed: 4007418361

# Time:  O(q + n * t)
# Space: O(t + n + q)

# radix sort

class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        max_t = max(t for _, t in queries)
        lookup = [[] for _ in xrange(max_t+1)]
        for i, (k, t) in enumerate(queries):
            lookup[t].append((k, i))
        result = [0]*len(queries)
        idxs = range(len(nums))
        for l in xrange(1, max_t+1):
            cnt = [0]*10
            for i in idxs:
                d = int(nums[i][-l])
                cnt[d] += 1
            for d in xrange(9):
                cnt[d+1] += cnt[d]
            new_idxs = [0]*len(nums)
            for i in reversed(idxs):
                d = int(nums[i][-l])
                cnt[d] -= 1
                new_idxs[cnt[d]] = i
            idxs = new_idxs
            for k, i in lookup[l]:
                result[i] = idxs[k-1]
        return result