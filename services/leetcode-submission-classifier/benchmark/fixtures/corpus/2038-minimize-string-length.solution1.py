# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-string-length
# source_path: LeetCode-Solutions-master/Python/minimize-string-length.py
# solution_class: Solution
# submission_id: 3b56e40fd8e768d8fe0ce31ada87034c23a060c9
# seed: 1571232392

# Time:  O(n)
# Space: O(1)

# hash table

class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(set(s))