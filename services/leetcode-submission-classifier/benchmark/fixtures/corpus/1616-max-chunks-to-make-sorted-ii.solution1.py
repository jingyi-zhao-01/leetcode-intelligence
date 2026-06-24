# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-chunks-to-make-sorted-ii
# source_path: LeetCode-Solutions-master/Python/max-chunks-to-make-sorted-ii.py
# solution_class: Solution
# submission_id: f490dd343d97fe350c4dc3cc4a775fe953310c47
# seed: 3637687811

# Time:  O(n)
# Space: O(n)

# mono stack solution

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result, increasing_stk = 0, []
        for num in arr:
            max_num = num if not increasing_stk else max(increasing_stk[-1], num)
            while increasing_stk and increasing_stk[-1] > num:
                increasing_stk.pop()
            increasing_stk.append(max_num)
        return len(increasing_stk)