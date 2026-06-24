# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: next-greater-element-i
# source_path: LeetCode-Solutions-master/Python/next-greater-element-i.py
# solution_class: Solution
# submission_id: 47818fbc1d69b9a495bc48baa9f19663bef5ef2e
# seed: 2990946556

# Time:  O(m + n)
# Space: O(m + n)

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stk, lookup = [], {}
        for num in nums:
            while stk and num > stk[-1]:
                lookup[stk.pop()] = num
            stk.append(num)
        while stk:
            lookup[stk.pop()] = -1
        return map(lambda x : lookup[x], findNums)