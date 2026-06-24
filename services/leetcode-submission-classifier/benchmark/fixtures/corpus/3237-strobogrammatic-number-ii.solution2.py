# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: strobogrammatic-number-ii
# source_path: LeetCode-Solutions-master/Python/strobogrammatic-number-ii.py
# solution_class: Solution2
# submission_id: 169e0270b05c40421ef00a46779b9d9c829900ef
# seed: 2841950558

# Time:  O(n * 5^(n/2))
# Space: O(n)

class Solution2(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        def findStrobogrammaticRecu(n, k):
            if k == 0:
                return ['']
            elif k == 1:
                return ['0', '1', '8']
            result = []
            for num in findStrobogrammaticRecu(n, k - 2):
                for key, val in lookup.iteritems():
                    if n != k or key != '0':
                        result.append(key + num + val)
            return result

        return findStrobogrammaticRecu(n, n)