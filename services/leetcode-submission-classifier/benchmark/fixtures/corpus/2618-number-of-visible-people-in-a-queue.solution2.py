# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-visible-people-in-a-queue
# source_path: LeetCode-Solutions-master/Python/number-of-visible-people-in-a-queue.py
# solution_class: Solution2
# submission_id: e70f364a7b1ee6feb1d6b601a9f1987c3008f779
# seed: 3868840420

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        result = [0]*len(heights)
        stk = []
        for i in reversed(xrange(len(heights))):
            cnt = 0
            while stk and heights[stk[-1]] < heights[i]:
                stk.pop()
                cnt += 1
            result[i] = cnt+1 if stk else cnt
            if stk and heights[stk[-1]] == heights[i]:
                stk.pop()
            stk.append(i)
        return result