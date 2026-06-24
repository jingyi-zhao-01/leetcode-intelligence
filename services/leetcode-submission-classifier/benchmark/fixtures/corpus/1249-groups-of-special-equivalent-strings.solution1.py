# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: groups-of-special-equivalent-strings
# source_path: LeetCode-Solutions-master/Python/groups-of-special-equivalent-strings.py
# solution_class: Solution
# submission_id: aca64b0ca63c310ec91c673c4852a28206d15ded
# seed: 2911807393

# Time:  O(n * l)
# Space: O(n)

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def count(word):
            result = [0]*52
            for i, letter in enumerate(word):
                result[ord(letter)-ord('a') + 26*(i%2)] += 1
            return tuple(result)

        return len({count(word) for word in A})