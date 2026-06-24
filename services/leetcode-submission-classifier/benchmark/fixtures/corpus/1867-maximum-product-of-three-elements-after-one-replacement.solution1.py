# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-of-three-elements-after-one-replacement
# source_path: LeetCode-Solutions-master/Python/maximum-product-of-three-elements-after-one-replacement.py
# solution_class: Solution
# submission_id: f5702251931b1ce6c8ce74f40680f7cafa961b98
# seed: 2683882837

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 2
        top = [0]*L
        for x in nums:
            x = abs(x)
            for i in xrange(L):
                if x > top[i]:
                    x, top[i] = top[i], x
        return top[0]*top[1]*10**5