# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: camelcase-matching
# source_path: LeetCode-Solutions-master/Python/camelcase-matching.py
# solution_class: Solution
# submission_id: 9e9bcd6ef31b45c579fade050311ff2f5f9a7606
# seed: 2540750797

# Time:  O(n * l), n is number of quries
#                , l is length of query
# Space: O(1)

class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        def is_matched(query, pattern):
            i = 0
            for c in query:
                if i < len(pattern) and pattern[i] == c:
                    i += 1
                elif c.isupper():
                    return False
            return i == len(pattern)
        
        result = []
        for query in queries:
            result.append(is_matched(query, pattern))
        return result