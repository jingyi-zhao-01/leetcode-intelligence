# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-adjacent-swaps-to-alternate-parity
# source_path: LeetCode-Solutions-master/Python/minimum-adjacent-swaps-to-alternate-parity.py
# solution_class: Solution
# submission_id: f738e860c6fa27a28bb631aeb1e2e408d6a30a52
# seed: 164827790

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def count(start):
            it = iter(j for j in xrange(start, len(nums), 2))
            return sum(abs(next(it)-i) for i in xrange(len(nums)) if nums[i]%2)

        cnt = sum(x%2 for x in nums)
        if cnt == len(nums)-cnt:
            return min(count(0), count(1))
        if cnt == (len(nums)-cnt)+1:
            return count(0)
        if cnt+1 == len(nums)-cnt:
            return count(1)
        return -1