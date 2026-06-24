# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-columns-to-make-sorted
# source_path: LeetCode-Solutions-master/Python/delete-columns-to-make-sorted.py
# solution_class: Solution2
# submission_id: 2c0b4156dc1d50a3e6ffbaf18734bcc8f710b50e
# seed: 4105620162

# Time:  O(n * l)
# Space: O(1)

class Solution2(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        for col in itertools.izip(*A):
            if any(col[i] > col[i+1] for i in xrange(len(col)-1)):
                result += 1
        return result