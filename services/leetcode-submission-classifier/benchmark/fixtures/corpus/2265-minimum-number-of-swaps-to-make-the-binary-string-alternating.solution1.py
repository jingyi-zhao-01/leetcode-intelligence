# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-swaps-to-make-the-binary-string-alternating
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-swaps-to-make-the-binary-string-alternating.py
# solution_class: Solution
# submission_id: b6bf91d1472798079bd92e798411e6a3fd5bd270
# seed: 3219395924

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        def cost(s, x): 
            diff = 0 
            for c in s:
                diff += int(c) != x
                x ^= 1
            return diff//2
    
        ones = s.count('1')
        zeros = len(s)-ones 
        if abs(ones-zeros) > 1:
            return -1
        if ones > zeros:
            return cost(s, 1)
        if ones < zeros:
            return cost(s, 0)
        return min(cost(s, 1), cost(s, 0))