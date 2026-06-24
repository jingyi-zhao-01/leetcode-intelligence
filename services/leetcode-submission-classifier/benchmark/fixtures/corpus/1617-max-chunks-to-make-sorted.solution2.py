# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-chunks-to-make-sorted
# source_path: LeetCode-Solutions-master/Python/max-chunks-to-make-sorted.py
# solution_class: Solution2
# submission_id: b7edff971c2e52984fe9f0a779bd6168bb5a60fc
# seed: 2878002113

# Time:  O(n)
# Space: O(1)

class Solution2(object):
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