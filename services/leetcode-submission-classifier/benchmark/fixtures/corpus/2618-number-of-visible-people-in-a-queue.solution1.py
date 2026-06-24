# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-visible-people-in-a-queue
# source_path: LeetCode-Solutions-master/Python/number-of-visible-people-in-a-queue.py
# solution_class: Solution
# submission_id: 25e6c83efabf0082e0017b9d6a1d9edce5905364
# seed: 3783877892

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        result = [0]*len(heights)
        stk = []
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] < h:
                result[stk.pop()] += 1
            if stk:
                result[stk[-1]] += 1
            if stk and heights[stk[-1]] == h:
                stk.pop()
            stk.append(i)
        return result