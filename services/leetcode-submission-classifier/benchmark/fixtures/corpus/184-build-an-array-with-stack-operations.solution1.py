# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: build-an-array-with-stack-operations
# source_path: LeetCode-Solutions-master/Python/build-an-array-with-stack-operations.py
# solution_class: Solution
# submission_id: 16ae73120b1f3cc6cf798ebd649efc06037f8663
# seed: 2317474280

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result, curr = [], 1
        for t in target:
            result.extend(["Push", "Pop"]*(t-curr))
            result.append("Push")
            curr = t+1
        return result