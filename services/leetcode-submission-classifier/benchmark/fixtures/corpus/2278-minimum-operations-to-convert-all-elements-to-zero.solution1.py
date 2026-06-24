# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-convert-all-elements-to-zero
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-convert-all-elements-to-zero.py
# solution_class: Solution
# submission_id: ddb39a7482fd5f0c77f051c202519aa9070b8480
# seed: 8550322

# Time:  O(n)
# Space: O(n)

# greedy, mono stack

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        stk = [0]
        for x in nums:
            while stk and stk[-1] > x:
                stk.pop()
            if stk[-1] < x:
                result += 1
                stk.append(x)
        return result