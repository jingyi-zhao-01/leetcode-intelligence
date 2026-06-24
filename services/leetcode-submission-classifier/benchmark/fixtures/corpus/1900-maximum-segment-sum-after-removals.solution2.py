# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-segment-sum-after-removals
# source_path: LeetCode-Solutions-master/Python/maximum-segment-sum-after-removals.py
# solution_class: Solution2
# submission_id: af364d0b14ef04341bf3aea87792f33e4dc16f6f
# seed: 3404319004

# Time:  O(n)
# Space: O(n)

class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
    def __init__(self, nums):
        self.set = range(len(nums))
        self.rank = [0]*len(nums)
        self.size = nums[:]

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:  # union by rank
            x, y = y, x
        self.set[x] = self.set[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.size[y] += self.size[x]
        return True

    def total(self, x):
        return self.size[self.find_set(x)]


# union find

class Solution2(object):
    def maximumSegmentSum(self, nums, removeQueries):
        """
        :type nums: List[int]
        :type removeQueries: List[int]
        :rtype: List[int]
        """
        removed_idxs = SortedList([-1, len(nums)])
        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        segments = SortedList([prefix[-1]])
        result = []
        for q in removeQueries: 
            removed_idxs.add(q)
            i = removed_idxs.bisect_left(q)
            left, right = removed_idxs[i-1], removed_idxs[i+1]
            segments.remove(prefix[right]-prefix[left+1])
            segments.add(prefix[q]-prefix[left+1])
            segments.add(prefix[right]-prefix[q+1])
            result.append(segments[-1])
        return result