# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-importance-of-roads
# source_path: LeetCode-Solutions-master/Python/maximum-total-importance-of-roads.py
# solution_class: Solution
# submission_id: 3a2444cd11ea1e7bf9c13ce56cb0267eca86a9db
# seed: 4203958091

# Time:  O(n)
# Space: O(n)

# greedy, counting sort

class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        def inplace_counting_sort(nums, reverse=False):  # Time: O(n)
            count = [0]*(max(nums)+1)
            for num in nums:
                count[num] += 1
            for i in xrange(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(xrange(len(nums))):  # inplace but unstable sort
                while nums[i] >= 0:
                    count[nums[i]] -= 1
                    j = count[nums[i]]
                    nums[i], nums[j] = nums[j], ~nums[i]
            for i in xrange(len(nums)):
                nums[i] = ~nums[i]  # restore values
            if reverse:  # unstable sort
                nums.reverse()

        degree = [0]*n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        inplace_counting_sort(degree)
        return sum(i*x for i, x in enumerate(degree, 1))