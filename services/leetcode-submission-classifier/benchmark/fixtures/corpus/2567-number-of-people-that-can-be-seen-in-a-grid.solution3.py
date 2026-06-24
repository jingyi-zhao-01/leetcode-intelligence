# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-people-that-can-be-seen-in-a-grid
# source_path: LeetCode-Solutions-master/Python/number-of-people-that-can-be-seen-in-a-grid.py
# solution_class: Solution3
# submission_id: db31851fafb6b1143ca18b5eab2d14698421a57e
# seed: 1006171077

# Time:  O(m * n)
# Space: O(m + n)

# mono stack, optimized from solution2

class Solution3(object):
    def seePeople(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        def count(heights, i, stk, add):
            while stk and heights(stk[-1]) < heights(i):
                increase(stk.pop())
            if stk:
                increase(stk[-1])
            if stk and heights(stk[-1]) == heights(i):
                stk.pop()
            stk.append(i)
            
        result = [[0]*len(heights[0]) for _ in xrange(len(heights))]
        for i in xrange(len(heights)):
            stk = []
            def increase(x): result[i][x] += 1
            for j in xrange(len(heights[0])):
                count(lambda x: heights[i][x], j, stk, add)
        for j in xrange(len(heights[0])):
            stk = []
            def increase(x): result[x][j] += 1
            for i in xrange(len(heights)):
                count(lambda x: heights[x][j], i, stk, add)
        return result