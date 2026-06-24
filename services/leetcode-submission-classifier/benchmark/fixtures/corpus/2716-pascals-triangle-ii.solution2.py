# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pascals-triangle-ii
# source_path: LeetCode-Solutions-master/Python/pascals-triangle-ii.py
# solution_class: Solution2
# submission_id: dd96df9d5ab8c5a60b6e734aa09483c76fc61644
# seed: 2151967106

# Time:  O(n^2)
# Space: O(1)

class Solution2(object):
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [1]
        for i in range(1, rowIndex + 1):
            result = [1] + [result[j - 1] + result[j] for j in xrange(1, i)] + [1]
        return result