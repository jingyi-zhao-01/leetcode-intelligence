# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: nested-list-weight-sum
# source_path: LeetCode-Solutions-master/Python/nested-list-weight-sum.py
# solution_class: Solution
# submission_id: 51014adc12953f58942c2f23774366db1443ca76
# seed: 839646920

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def depthSumHelper(nestedList, depth):
            res = 0
            for l in nestedList:
                if l.isInteger():
                    res += l.getInteger() * depth
                else:
                    res += depthSumHelper(l.getList(), depth + 1)
            return res
        return depthSumHelper(nestedList, 1)