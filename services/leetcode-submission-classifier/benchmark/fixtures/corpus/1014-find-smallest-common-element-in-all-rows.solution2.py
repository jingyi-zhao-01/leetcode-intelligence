# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-smallest-common-element-in-all-rows
# source_path: LeetCode-Solutions-master/Python/find-smallest-common-element-in-all-rows.py
# solution_class: Solution2
# submission_id: 4b794f6f3012c57adda6316dbe2297f5cec8b304
# seed: 903160078

# Time:  O(m * n)
# Space: O(n)

class Solution2(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # assumed value is unique in each row
        counter = collections.Counter()
        for row in mat:
            for c in row:
                counter[c] += 1
                if counter[c] == len(mat):
                    return c
        return -1