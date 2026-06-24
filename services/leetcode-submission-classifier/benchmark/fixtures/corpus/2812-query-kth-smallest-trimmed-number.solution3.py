# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: query-kth-smallest-trimmed-number
# source_path: LeetCode-Solutions-master/Python/query-kth-smallest-trimmed-number.py
# solution_class: Solution3
# submission_id: 5a8b3dd6a501232b390f5439ad024747f551c166
# seed: 1812332647

# Time:  O(q + n * t)
# Space: O(t + n + q)

# radix sort

class Solution3(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def compare(a, b):
            for i in xrange(len(nums[a])-t, len(nums[a])):
                if nums[a][i] < nums[b][i]:
                    return -1
                if nums[a][i] > nums[b][i]:
                    return 1
            return cmp(a, b)

        max_t = max(t for _, t in queries)
        lookup = [[] for _ in xrange(max_t+1)]
        for i, (k, t) in enumerate(queries):
            lookup[t].append((k, i))
        result = [0]*len(queries)
        idxs = range(len(nums))
        for t in xrange(1, max_t+1):
            if not lookup[t]:
                continue
            idxs.sort(cmp=compare)
            for k, i in lookup[t]:
                result[i] = idxs[k-1]
        return result