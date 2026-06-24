# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-number-of-subarrays-where-boundary-elements-are-maximum
# source_path: LeetCode-Solutions-master/Python/find-the-number-of-subarrays-where-boundary-elements-are-maximum.py
# solution_class: Solution
# submission_id: c3318ca91a140676e51fd9276b54fd05f7bdf53b
# seed: 502163649

# Time:  O(n)
# Space: O(n)

# mono stack, combinatorics

class Solution(object):
    def numberOfSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        stk = []
        for x in nums:
            while stk and stk[-1][0] < x:
                stk.pop()
            if not stk or stk[-1][0] != x:
                stk.append([x, 0])
            stk[-1][1] += 1
            result += stk[-1][1]
        return result