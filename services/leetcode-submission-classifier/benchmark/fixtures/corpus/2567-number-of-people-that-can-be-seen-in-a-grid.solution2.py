# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-people-that-can-be-seen-in-a-grid
# source_path: LeetCode-Solutions-master/Python/number-of-people-that-can-be-seen-in-a-grid.py
# solution_class: Solution2
# submission_id: f88ba297ee1dac25e00002765e689434eacb5922
# seed: 1073150721

# Time:  O(m * n)
# Space: O(m + n)

# mono stack, optimized from solution2

class Solution2(object):
    def seePeople(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        def count(heights, i, stk):
            cnt = 0
            while stk and heights(stk[-1]) < heights(i):
                stk.pop()
                cnt += 1
            if stk:
                cnt += 1
            if stk and heights(stk[-1]) == heights(i):
                stk.pop()
            stk.append(i)
            return cnt
            
        result = [[0]*len(heights[0]) for _ in xrange(len(heights))]
        for i in xrange(len(heights)):
            stk = []
            for j in reversed(xrange(len(heights[0]))):
                result[i][j] += count(lambda x: heights[i][x], j, stk)     
        for j in xrange(len(heights[0])):
            stk = []
            for i in reversed(xrange(len(heights))):
                result[i][j] += count(lambda x: heights[x][j], i, stk)             
        return result