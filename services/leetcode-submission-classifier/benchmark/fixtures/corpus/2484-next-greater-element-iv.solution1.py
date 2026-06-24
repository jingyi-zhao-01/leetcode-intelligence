# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: next-greater-element-iv
# source_path: LeetCode-Solutions-master/Python/next-greater-element-iv.py
# solution_class: Solution
# submission_id: 0a518fa2bde64098a7494cc95c536caf8b703785
# seed: 698432007

# Time:  O(n)
# Space: O(n)

# mono stack

class Solution(object):
    def secondGreaterElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result, stk1, stk2 = [-1]*len(nums), [], []
        for i, x in enumerate(nums):
            while stk2 and nums[stk2[-1]] < x:
                result[stk2.pop()] = x
            tmp = []
            while stk1 and nums[stk1[-1]] < x:
                tmp.append(stk1.pop())
            stk1.append(i)
            for x in reversed(tmp):
                stk2.append(x)
        return result