# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-make-all-array-elements-equal-to-1
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-make-all-array-elements-equal-to-1.py
# solution_class: Solution
# submission_id: 639ebcfcd5e137e68b1047e81a0119b4cc22650e
# seed: 3392754337

# Time:  O(n^2)
# Space: O(1)

# math, number theory, constructive algorithms

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        cnt = nums.count(1)
        if cnt:
            return len(nums)-cnt
        result = float("inf")
        for i in xrange(len(nums)): 
            g = nums[i]
            for j in range(i+1, len(nums)):
                g = gcd(g, nums[j])
                if g == 1:
                    result = min(result, j-i)
                    break
        return result+(len(nums)-1) if result != float("inf") else -1