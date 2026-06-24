# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: combinations
# source_path: LeetCode-Solutions-master/Python/combinations.py
# solution_class: Solution3
# submission_id: dd4b46fdc15dd77b54cf24d81c474354a968a4bf
# seed: 1076992829

# Time:  O(k * C(n, k))
# Space: O(k)

class Solution3(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combineDFS(n, start, intermediate, k, result):
            if k == 0:
                result.append(intermediate[:])
                return
            for i in xrange(start, n):
                intermediate.append(i+1)
                combineDFS(n, i+1, intermediate, k-1, result)
                intermediate.pop()

        result = []
        combineDFS(n, 0, [], k, result)
        return result