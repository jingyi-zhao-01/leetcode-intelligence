# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sum-of-four-digit-number-after-splitting-digits
# source_path: LeetCode-Solutions-master/Python/minimum-sum-of-four-digit-number-after-splitting-digits.py
# solution_class: Solution
# submission_id: c2b05ea616b629633677eb0a4fc40390a62299f5
# seed: 4163561011

# Time:  O(d) = O(1), d is the number of digits
# Space: O(d) = O(1)

# greedy

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
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
    
        nums = map(int, list(str(num)))
        inplace_counting_sort(nums)
        a = b = 0
        for x in nums:
            a = a*10+x
            a, b = b, a
        return a+b