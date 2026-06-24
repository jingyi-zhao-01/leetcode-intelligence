# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-size-subarray-sum
# source_path: LeetCode-Solutions-master/Python/minimum-size-subarray-sum.py
# solution_class: Solution2
# submission_id: 0f04c23a1886337ed1d73bf4c3920d329d10ffd3
# seed: 3369806288

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        min_size = float("inf")
        sum_from_start = [n for n in nums]
        for i in xrange(len(sum_from_start) - 1):
            sum_from_start[i + 1] += sum_from_start[i]
        for i in xrange(len(sum_from_start)):
            end = self.binarySearch(lambda x, y: x <= y, sum_from_start, \
                                    i, len(sum_from_start), \
                                    sum_from_start[i] - nums[i] + s)
            if end < len(sum_from_start):
                min_size = min(min_size, end - i + 1)

        return min_size if min_size != float("inf") else 0

    def binarySearch(self, compare, A, start, end, target):
        while start < end:
            mid = start + (end - start) / 2
            if compare(target, A[mid]):
                end = mid
            else:
                start = mid + 1
        return start