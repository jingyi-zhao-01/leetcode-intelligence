# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-segment-sum-after-removals
# source_path: LeetCode-Solutions-master/Python/maximum-segment-sum-after-removals.py
# solution_class: Solution
# submission_id: ad870ccc670881a3713fcfe3a3b717c04f2ed8d3
# seed: 3753606008

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

class Solution(object):
    def maximumSegmentSum(self, nums, removeQueries):
        """
        :type nums: List[int]
        :type removeQueries: List[int]
        :rtype: List[int]
        """
        result = [0]*len(removeQueries)
        lookup = [0]*len(nums)
        uf = UnionFind(nums)
        for i in reversed(xrange(1, len(removeQueries))): 
            q = removeQueries[i]
            lookup[q] = 1
            if q-1 >= 0 and lookup[q-1]:
                uf.union_set(q-1, q)
            if q+1 < len(nums) and lookup[q+1]:
                uf.union_set(q, q+1)
            result[i-1] = max(result[i], uf.total(q))   
        return result