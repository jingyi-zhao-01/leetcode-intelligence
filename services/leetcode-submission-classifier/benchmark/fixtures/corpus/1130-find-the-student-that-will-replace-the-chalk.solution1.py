# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-student-that-will-replace-the-chalk
# source_path: LeetCode-Solutions-master/Python/find-the-student-that-will-replace-the-chalk.py
# solution_class: Solution
# submission_id: 08816e2b80ee57de0645b42259653c494179f932
# seed: 2665602100

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        k %= sum(chalk)
        for i, x in enumerate(chalk):
            if k < x:
                return i
            k -= x
        return -1