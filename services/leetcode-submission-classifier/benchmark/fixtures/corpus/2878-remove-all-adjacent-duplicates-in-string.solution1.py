# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-all-adjacent-duplicates-in-string
# source_path: LeetCode-Solutions-master/Python/remove-all-adjacent-duplicates-in-string.py
# solution_class: Solution
# submission_id: a93ce0dd903801a00e61c7962ef406b524521493
# seed: 482203836

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        for c in S:
            if result and result[-1] == c:
                result.pop()
            else:
                result.append(c)
        return "".join(result)