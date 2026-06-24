# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: range-sum-of-sorted-subarray-sums
# source_path: LeetCode-Solutions-master/Python/range-sum-of-sorted-subarray-sums.py
# solution_class: Solution
# submission_id: 300fddae9f981e2e5c67b10274a40d90c9a622d3
# seed: 2437103502

# Time:  O(nlog(sum(nums)))
# Space: O(n)

# binary search + sliding window solution

class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        def countUntil(nums, target):
            result, curr, left = 0, 0, 0
            for right in xrange(len(nums)):
                curr += nums[right]
                while curr > target:
                    curr -= nums[left]
                    left += 1
                result += right-left+1
            return result
        
        def sumUntil(nums, prefix, target):
            result, curr, total, left = 0, 0, 0, 0
            for right in xrange(len(nums)):
                curr += nums[right]
                total += nums[right]*(right-left+1)
                while curr > target:
                    curr -= nums[left]
                    total -= prefix[right+1]-prefix[(left-1)+1]
                    left += 1
                result += total
            return result
            
        def sumLessOrEqualTo(prefix, nums, left, right, count):
            while left <= right:
                mid = left + (right-left)//2
                if countUntil(nums, mid)-count >= 0:
                    right = mid-1
                else:
                    left = mid+1
            return sumUntil(nums, prefix, left)-left*(countUntil(nums, left)-count)
    
        MOD = 10**9+7
        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        m, M = min(nums), sum(nums)
        return (sumLessOrEqualTo(prefix, nums, m, M, right) -
                sumLessOrEqualTo(prefix, nums, m, M, left-1))%MOD