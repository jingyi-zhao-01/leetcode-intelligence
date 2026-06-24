# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: earliest-second-to-mark-indices-ii
# source_path: LeetCode-Solutions-master/Python/earliest-second-to-mark-indices-ii.py
# solution_class: Solution
# submission_id: df8f5706aae1a6d82ac0206b792ad9013a72df77
# seed: 3169217820

# Time:  O((m + nlogn) * logm)
# Space: O(n)

import heapq


# binary search, greedy, heap

class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        """
        :type nums: List[int]
        :type changeIndices: List[int]
        :rtype: int
        """
        def check(t):
            min_heap = []
            cnt = 0
            for i in reversed(xrange(t)):
                if i != lookup[changeIndices[i]-1]:
                    cnt += 1
                    continue
                heapq.heappush(min_heap, nums[changeIndices[i]-1])
                if cnt:
                    cnt -= 1
                else:
                    cnt += 1
                    heapq.heappop(min_heap)
            return total-(sum(min_heap)+len(min_heap)) <= cnt

        lookup = [-1]*len(nums)
        for i in reversed(xrange(len(changeIndices))):
            if nums[changeIndices[i]-1]:
                lookup[changeIndices[i]-1] = i
        total = sum(nums)+len(nums)
        left, right = sum((1 if lookup[i] != -1 else nums[i]) for i in xrange(len(nums)))+len(nums), len(changeIndices) 
        while left <= right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left if left <= len(changeIndices) else -1