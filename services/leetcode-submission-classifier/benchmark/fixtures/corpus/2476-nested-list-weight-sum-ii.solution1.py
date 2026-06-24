# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: nested-list-weight-sum-ii
# source_path: LeetCode-Solutions-master/Python/nested-list-weight-sum-ii.py
# solution_class: Solution
# submission_id: 6c187ecc98168e1b77613a501c673bc47be4c295
# seed: 3896869519

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def depthSumInverseHelper(list, depth, result):
            if len(result) < depth + 1:
                result.append(0)
            if list.isInteger():
                result[depth] += list.getInteger()
            else:
                for l in list.getList():
                    depthSumInverseHelper(l, depth + 1, result)

        result = []
        for list in nestedList:
            depthSumInverseHelper(list, 0, result)

        sum = 0
        for i in reversed(xrange(len(result))):
            sum += result[i] * (len(result) - i)
        return sum