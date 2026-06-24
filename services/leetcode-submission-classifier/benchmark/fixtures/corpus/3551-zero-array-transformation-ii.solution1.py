# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: zero-array-transformation-ii
# source_path: LeetCode-Solutions-master/Python/zero-array-transformation-ii.py
# solution_class: Solution
# submission_id: 0712ef1852d52af007d18ee2515789acc8b3ab77
# seed: 2069768709

# Time:  O((n + q) * logn)
# Space: O(n)

# binary search, line sweep

class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def check(k):
            events = [0]*(len(nums)+1)
            for i in xrange(k):
                events[queries[i][0]] += queries[i][2]
                events[queries[i][1]+1] -= queries[i][2]
            curr = 0
            for i in xrange(len(nums)):
                curr += events[i]
                if nums[i] > curr:
                    return False
            return True
        
        result = binary_search(0, len(queries), check)
        return result if result <= len(queries) else -1