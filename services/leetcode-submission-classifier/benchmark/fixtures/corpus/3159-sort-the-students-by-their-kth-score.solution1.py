# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-the-students-by-their-kth-score
# source_path: LeetCode-Solutions-master/Python/sort-the-students-by-their-kth-score.py
# solution_class: Solution
# submission_id: 707dc3bed21bfe42738c507f28b6ff0b1772457d
# seed: 1472735654

# Time:  O(mlogm)
# Space: O(1)

# sort

class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        score.sort(key=lambda x: x[k], reverse=True)
        return score