# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-people-that-can-be-seen-in-a-grid
# source_path: LeetCode-Solutions-master/Python/number-of-people-that-can-be-seen-in-a-grid.py
# solution_class: Solution
# submission_id: 395bff4c26143429ff56a84eecb6f9cb7c68a5d7
# seed: 902116707

# Time:  O(m * n)
# Space: O(m + n)

# mono stack, optimized from solution2

class Solution(object):
    def seePeople(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        def count(h, stk):
            cnt = 0
            while stk and stk[-1] < h:
                stk.pop()
                cnt += 1
            if stk:
                cnt += 1
            if not stk or stk[-1] != h:
                stk.append(h)
            return cnt
            
        result = [[0]*len(heights[0]) for _ in xrange(len(heights))]
        for i in xrange(len(heights)):
            stk = []
            for j in reversed(xrange(len(heights[0]))):
                result[i][j] += count(heights[i][j], stk)     
        for j in xrange(len(heights[0])):
            stk = []
            for i in reversed(xrange(len(heights))):
                result[i][j] += count(heights[i][j], stk)             
        return result