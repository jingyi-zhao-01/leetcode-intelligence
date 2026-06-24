# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-and-replace-in-string
# source_path: LeetCode-Solutions-master/Python/find-and-replace-in-string.py
# solution_class: Solution
# submission_id: 67990b93a565c051984a88078e9315adfe965694
# seed: 507299152

# Time:  O(n + m), m is the number of targets
# Space: O(n)

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        bucket = [None] * len(S)
        for i in xrange(len(indexes)):
            if all(indexes[i]+k < len(S) and S[indexes[i]+k] == sources[i][k]
                   for k in xrange(len(sources[i]))):
                bucket[indexes[i]] = (len(sources[i]), list(targets[i]))
        result = []
        i = 0
        while i < len(S):
            if bucket[i]:
                result.extend(bucket[i][1])
                i += bucket[i][0]
            else:
                result.append(S[i])
                i += 1
        return "".join(result)