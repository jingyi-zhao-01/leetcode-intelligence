# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-form-subsequence-with-target-sum
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-form-subsequence-with-target-sum.py
# solution_class: Solution3
# submission_id: 7c0dfc488d2cfa56224f9b9a5819d4ec86d9cdf1
# seed: 3168928059

# Time:  O(n)
# Space: O(logn)

# codeforces, https://codeforces.com/problemset/problem/1303/D
# counting sort, greedy

class Solution3(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)
        if total < target:
            return -1

        result = 0
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        while target:
            x = -heapq.heappop(max_heap)
            if x <= target:
                target -= x
                total -= x
            elif total-x >= target:
                total -= x
            else:
                heapq.heappush(max_heap, -x//2)
                heapq.heappush(max_heap, -x//2)
                result += 1
        return result